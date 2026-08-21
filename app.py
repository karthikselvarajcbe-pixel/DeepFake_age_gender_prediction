import streamlit as st

from PIL import Image

from utils.deepfake_predictor import predict_deepfake
from utils.gender_predictor import predict_gender
from utils.age_predictor import predict_age


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="AI Face Analysis",
    page_icon="🤖",
    layout="wide"
)


# ============================================================
# SESSION STATE
# ============================================================

if "uploader_key" not in st.session_state:
    st.session_state.uploader_key = 0

if "prediction_results" not in st.session_state:
    st.session_state.prediction_results = []


# ============================================================
# CLEAR ALL
# ============================================================

def clear_all():

    st.session_state.uploader_key += 1

    st.session_state.prediction_results = []


# ============================================================
# TITLE
# ============================================================

st.title("AI Face Analysis")

st.write(
    "Upload one or more images and click Predict."
)


# ============================================================
# UPLOAD SECTION
# ============================================================

col1, col2 = st.columns([5, 1])


with col1:

    uploaded_files = st.file_uploader(
        "Upload Images",
        type=["jpg", "jpeg", "png"],
        accept_multiple_files=True,
        key=f"image_uploader_{st.session_state.uploader_key}"
    )


with col2:

    st.write("")

    st.button(
        "Clear All",
        on_click=clear_all,
        use_container_width=True
    )


# ============================================================
# SHOW SELECTED FILE COUNT ONLY
# ============================================================

if uploaded_files:

    st.info(
        f"{len(uploaded_files)} image(s) ready for prediction."
    )


# ============================================================
# PREDICT BUTTON
# ============================================================

if uploaded_files:

    if st.button(
        "Predict",
        type="primary",
        use_container_width=True
    ):

        prediction_results = []

        progress = st.progress(0)

        status = st.empty()

        total = len(uploaded_files)


        # ====================================================
        # PROCESS EACH IMAGE
        # ====================================================

        for index, uploaded_file in enumerate(
            uploaded_files
        ):

            filename = uploaded_file.name

            status.write(
                f"Processing: {filename}"
            )


            try:

                # --------------------------------------------
                # LOAD IMAGE
                # --------------------------------------------

                image = Image.open(
                    uploaded_file
                ).convert("RGB")


                # --------------------------------------------
                # DEEPFAKE
                # --------------------------------------------

                deepfake_label, deepfake_conf = (
                    predict_deepfake(image)
                )


                # ============================================
                # FAKE
                # ============================================

                if deepfake_label == "FAKE":

                    prediction_results.append({

                        "image": image,

                        "filename": filename,

                        "result": "FAKE",

                        "gender": "NA",

                        "age": "NA",

                        "confidence": deepfake_conf

                    })


                # ============================================
                # REAL
                # ============================================

                else:

                    # ----------------------------------------
                    # AGE
                    # ----------------------------------------

                    age = predict_age(
                        image
                    )


                    # ----------------------------------------
                    # GENDER
                    # ----------------------------------------

                    gender, gender_conf = (
                        predict_gender(
                            image
                        )
                    )


                    # ----------------------------------------
                    # AGE VALUE
                    # ----------------------------------------

                    if age is None:

                        age_display = "NA"

                    else:

                        age_display = age


                    # ----------------------------------------
                    # SAVE RESULT
                    # ----------------------------------------

                    prediction_results.append({

                        "image": image,

                        "filename": filename,

                        "result": "REAL",

                        "gender": gender,

                        "age": age_display,

                        "confidence": deepfake_conf

                    })


            except Exception as e:

                prediction_results.append({

                    "image": image if "image" in locals() else None,

                    "filename": filename,

                    "result": "ERROR",

                    "gender": "NA",

                    "age": "NA",

                    "confidence": "NA",

                    "error": str(e)

                })


            # --------------------------------------------
            # PROGRESS
            # --------------------------------------------

            progress.progress(
                (index + 1) / total
            )


        # ====================================================
        # SAVE RESULTS
        # ====================================================

        st.session_state.prediction_results = (
            prediction_results
        )


        status.success(
            "Prediction completed!"
        )


# ============================================================
# PREDICTION RESULTS
# ============================================================

if st.session_state.prediction_results:

    st.divider()

    st.subheader(
        "Prediction Results"
    )


    # ========================================================
    # RESULT GRID
    # ========================================================

    result_columns = st.columns(4)


    for index, item in enumerate(
        st.session_state.prediction_results
    ):

        with result_columns[index % 4]:

            # --------------------------------------------
            # IMAGE
            # --------------------------------------------

            if item["image"] is not None:

                display_image = item[
                    "image"
                ].resize(
                    (224, 224)
                )

                st.image(
                    display_image,
                    width=224
                )


            # --------------------------------------------
            # FILE NAME
            # --------------------------------------------

            st.caption(
                item["filename"]
            )


            # --------------------------------------------
            # RESULT
            # --------------------------------------------

            if item["result"] == "REAL":

                st.success(
                    "REAL"
                )

            elif item["result"] == "FAKE":

                st.error(
                    "FAKE"
                )

            else:

                st.warning(
                    "ERROR"
                )


            # --------------------------------------------
            # INFORMATION
            # --------------------------------------------

            st.write(
                f"**Gender:** {item['gender']}"
            )

            st.write(
                f"**Age:** {item['age']}"
            )

            st.write(
                f"**Confidence:** "
                f"{item['confidence']}%"
            )

            st.divider()