import streamlit as st
import numpy as np
from PIL import Image, ImageOps, ImageFilter
from sklearn.datasets import load_digits
from sklearn.svm import SVC
import base64
import io

st.set_page_config(
    page_title="DigitAI",
    page_icon="🔢",
    layout="centered"
)

@st.cache_resource
def train_model():
    data = load_digits()

    model = SVC(
        C=10,
        gamma="scale",
        probability=True,
        random_state=42
    )

    model.fit(data.data, data.target)

    return model

model = train_model()


def prepare_image(image):

    image = image.convert("L")

    image = ImageOps.autocontrast(image)

    arr = np.array(image)

    if arr.mean() > 127:
        image = ImageOps.invert(image)

    arr = np.array(image)

    mask = arr > 25

    if not mask.any():
        return None

    ys, xs = np.where(mask)

    left = max(0, xs.min() - 8)
    right = min(arr.shape[1], xs.max() + 8)
    top = max(0, ys.min() - 8)
    bottom = min(arr.shape[0], ys.max() + 8)

    image = image.crop(
        (left, top, right, bottom)
    )

    width, height = image.size

    size = max(width, height)

    square = Image.new(
        "L",
        (size, size),
        0
    )

    x = (size - width) // 2
    y = (size - height) // 2

    square.paste(
        image,
        (x, y)
    )

    square = square.resize(
        (8, 8),
        Image.Resampling.LANCZOS
    )

    pixels = np.array(
        square,
        dtype=np.float32
    )

    pixels = pixels / 255.0 * 16.0

    return square, pixels.reshape(1, 64)


st.markdown(
    """
    <style>

    .title {
        text-align: center;
        font-size: 46px;
        font-weight: 800;
        margin-bottom: 0;
    }

    .subtitle {
        text-align: center;
        color: #777;
        font-size: 18px;
        margin-top: 5px;
        margin-bottom: 30px;
    }

    .result-card {
        background: #f7f7f7;
        border-radius: 20px;
        padding: 30px;
        text-align: center;
        margin-top: 20px;
        border: 1px solid #eeeeee;
    }

    .result-title {
        font-size: 18px;
        color: #777;
        margin-bottom: 5px;
    }

    .result-number {
        font-size: 75px;
        font-weight: 800;
        line-height: 1.1;
    }

    .confidence-text {
        font-size: 17px;
        color: #666;
        margin-top: 5px;
    }

    .footer {
        text-align: center;
        color: #888;
        font-size: 14px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


st.markdown(
    '<div class="title">🔢 DigitAI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'AI-Powered Handwritten Digit Recognizer'
    '</div>',
    unsafe_allow_html=True
)

st.write(
    "Draw a digit or upload an image and let AI recognize it."
)

draw_tab, upload_tab = st.tabs(
    ["✏️ Draw Digit", "📤 Upload Image"]
)

with draw_tab:

    st.markdown("### ✏️ Draw your digit")

    st.caption(
        "Draw one clear digit in the center of the canvas."
    )

    canvas = st.components.v2.component(
        name="digit_canvas",
        html="""
        <div class="wrapper">

            <canvas
                id="canvas"
                width="280"
                height="280">
            </canvas>

            <div class="buttons">

                <button id="clear">
                    🗑️ Clear
                </button>

                <button id="predict">
                    🔮 Predict
                </button>

            </div>

        </div>
        """,
        css="""
        .wrapper {
            text-align: center;
            font-family: sans-serif;
        }

        canvas {
            width: 280px;
            height: 280px;
            background: black;
            border: 2px solid #ddd;
            border-radius: 18px;
            cursor: crosshair;
            touch-action: none;
        }

        .buttons {
            margin-top: 15px;
            display: flex;
            justify-content: center;
            gap: 12px;
        }

        button {
            padding: 10px 18px;
            border: none;
            border-radius: 10px;
            cursor: pointer;
            font-size: 14px;
        }
        """,
        js="""
        export default function({
            setStateValue,
            setTriggerValue,
            parentElement
        }) {

            const canvas =
                parentElement.querySelector("#canvas");

            const ctx =
                canvas.getContext("2d");

            const clearButton =
                parentElement.querySelector("#clear");

            const predictButton =
                parentElement.querySelector("#predict");

            ctx.fillStyle = "black";

            ctx.fillRect(
                0,
                0,
                canvas.width,
                canvas.height
            );

            ctx.strokeStyle = "white";
            ctx.lineWidth = 18;
            ctx.lineCap = "round";
            ctx.lineJoin = "round";

            let drawing = false;

            function getPosition(event) {

                const rect =
                    canvas.getBoundingClientRect();

                return {
                    x:
                        (event.clientX - rect.left)
                        * canvas.width
                        / rect.width,

                    y:
                        (event.clientY - rect.top)
                        * canvas.height
                        / rect.height
                };
            }

            canvas.addEventListener(
                "pointerdown",
                event => {

                    drawing = true;

                    const p =
                        getPosition(event);

                    ctx.beginPath();

                    ctx.moveTo(
                        p.x,
                        p.y
                    );
                }
            );

            canvas.addEventListener(
                "pointermove",
                event => {

                    if (!drawing) return;

                    const p =
                        getPosition(event);

                    ctx.lineTo(
                        p.x,
                        p.y
                    );

                    ctx.stroke();
                }
            );

            canvas.addEventListener(
                "pointerup",
                () => {
                    drawing = false;
                }
            );

            canvas.addEventListener(
                "pointerleave",
                () => {
                    drawing = false;
                }
            );

            clearButton.onclick = () => {

                ctx.fillStyle = "black";

                ctx.fillRect(
                    0,
                    0,
                    canvas.width,
                    canvas.height
                );

                ctx.strokeStyle = "white";
                ctx.lineWidth = 18;

                setStateValue(
                    "image",
                    ""
                );
            };

            predictButton.onclick = () => {

                const image =
                    canvas.toDataURL("image/png");

                setStateValue(
                    "image",
                    image
                );

                setTriggerValue(
                    "predict",
                    Date.now()
                );
            };
        }
        """
    )

    result = canvas(
        key="digit_canvas"
    )

    if result:

        image_data = getattr(
            result,
            "image",
            ""
        )

        trigger = getattr(
            result,
            "predict",
            None
        )

        if image_data and trigger:

            encoded = image_data.split(",")[1]

            image_bytes = base64.b64decode(
                encoded
            )

            image = Image.open(
                io.BytesIO(image_bytes)
            ).convert("L")

            st.session_state[
                "current_image"
            ] = image


with upload_tab:

    st.markdown("### 📤 Upload a handwritten digit")

    uploaded = st.file_uploader(
        "Choose an image",
        type=[
            "png",
            "jpg",
            "jpeg"
        ]
    )

    if uploaded:

        image = Image.open(
            uploaded
        ).convert("L")

        st.session_state[
            "current_image"
        ] = image


if "current_image" in st.session_state:

    image = st.session_state[
        "current_image"
    ]

    result = prepare_image(image)

    if result:

        processed, features = result

        probabilities = model.predict_proba(
            features
        )[0]

        classes = model.classes_

        order = np.argsort(
            probabilities
        )[::-1]

        top_three = order[:3]

        prediction = int(
            classes[top_three[0]]
        )

        confidence = (
            probabilities[top_three[0]]
            * 100
        )

        st.divider()

        st.markdown("### 🤖 AI Result")

        col1, col2 = st.columns(2)

        with col1:

            st.markdown("**Your Digit**")

            st.image(
                image,
                width=220
            )

        with col2:

            st.markdown("**Processed Digit**")

            st.image(
                processed.resize(
                    (240, 240),
                    Image.Resampling.NEAREST
                ),
                width=220
            )

        st.html(
            f"""
            <div class="result-card">

                <div class="result-title">
                    AI Prediction
                </div>

                <div class="result-number">
                    {prediction}
                </div>

                <div class="confidence-text">
                    Confidence: {confidence:.2f}%
                </div>

            </div>
            """
        )

        st.write("")

        st.markdown(
            "### 🏆 Top 3 Predictions"
        )

        for rank, index in enumerate(
            top_three,
            1
        ):

            digit = int(
                classes[index]
            )

            score = (
                probabilities[index]
                * 100
            )

            st.write(
                f"**{rank}. Digit {digit}** "
                f"— {score:.2f}%"
            )

            st.progress(
                float(
                    probabilities[index]
                )
            )

    else:

        st.warning(
            "Please draw a clear digit."
        )


st.divider()

st.markdown(
    """
    <div class="footer">
        Built with Python • Scikit-learn • Streamlit
    </div>
    """,
    unsafe_allow_html=True
)