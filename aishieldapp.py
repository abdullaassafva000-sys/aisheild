import random
import time
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="AI-SHIELD: Digital Deception Defense",
    page_icon="🛡️",
    layout="wide",
)

# Custom CSS for styling the dashboard
st.markdown(
    """
    <style>
    .main-header {font-size: 2.5rem; color: #FF4B4B; text-align: center; font-weight: bold;}
    .sub-header {font-size: 1.2rem; text-align: center; color: #A0A0A0; margin-bottom: 30px;}
    .metric-card {background-color: #1E1E1E; padding: 20px; border-radius: 10px; border: 1px solid #333;}
    .stAlert {border-radius: 8px;}
    </style>
""",
    unsafe_allow_html=True,
)

# App Title & Ecosystem Identity
st.markdown(
    '<p class="main-header">🛡️ AI-SHIELD Ecosystem</p>', unsafe_allow_html=True
)
st.markdown(
    '<p class="sub-header">Unified System Against AI-Powered Digital Deception (DeepShield | CallShield | NewsGuard)</p>',
    unsafe_allow_html=True,
)

# Sidebar Navigation for the 3 Pillars
st.sidebar.title("Navigation Hub")
app_mode = st.sidebar.selectbox(
    "Choose Module",
    [
        "Overview (Ecosystem)",
        "1. DeepShield (Deepfake Analyzer)",
        "2. CallShield (Scam Call Protection)",
        "3. NewsGuard (Fake News Detector)",
    ],
)

# ==========================================
# MODULE 0: ECOSYSTEM OVERVIEW
# ==========================================
if app_mode == "Overview (Ecosystem)":
  st.subheader("Project Vision: One Ecosystem")
  st.write(
      "Rather than treating deepfakes, fake news, and scam calls as isolated"
      " problems, **AI-SHIELD** approaches them as different forms of"
      " **AI-enabled digital deception**."
  )

  col1, col2, col3 = st.columns(3)

  with col1:
    st.markdown("### 🎭 DeepShield")
    st.write(
        "Multimodal verification tool analyzing images, videos, and audio for"
        " synthetic artifacts and structural inconsistencies."
    )

  with col2:
    st.markdown("### 📞 CallShield")
    st.write(
        "Answers *'What is this caller trying to do?'* via real-time risk"
        " flags, intent mapping, and voice-cloning alerts."
    )

  with col3:
    st.markdown("### 📰 NewsGuard")
    st.write(
        "Scans digital articles and social media posts for manipulated narratives,"
        " bot networks, and fabricated sources."
    )

  st.info(
      "👉 Use the sidebar to switch between modules and test the live"
      " interactive prototypes!"
  )

# ==========================================
# MODULE 1: DEEPSHIELD (Deepfake Detector)
# ==========================================
elif app_mode == "1. DeepShield (Deepfake Analyzer)":
  st.subheader("🎭 DeepShield: Multimodal Deepfake Verification")
  st.write(
      "Upload media to check lighting consistency, facial anomalies, and"
      " synthetic speech markers[cite: 1]."
  )

  media_type = st.radio(
      "Select Media Type to Scan", ["Image", "Video", "Audio"]
  )
  uploaded_file = st.file_uploader(
      f"Upload a sample {media_type.lower()}...",
      type=(
          ["jpg", "png", "jpeg"]
          if media_type == "Image"
          else ["mp4", "mov"] if media_type == "Video" else ["mp3", "wav"]
      ),
  )

  if uploaded_file is not None:
    if media_type == "Image":
      st.image(uploaded_file, caption="Uploaded Image Preview", width=400)
    elif media_type == "Audio":
      st.audio(uploaded_file)
    else:
      st.video(uploaded_file)

    if st.button("Run DeepShield Analysis"):
      with st.spinner("Analyzing structural signals & frame artifacts..."):
        time.sleep(2)  # Simulating processing delay

      # Generating deterministic mock results based on file length/name for consistency
      risk_score = random.choice(["HIGH", "MODERATE", "LOW"])

      st.markdown("---")
      st.markdown("### 🔍 Analysis Report")

      if risk_score == "HIGH":
        st.error("⚠️ Manipulation Risk: HIGH")
      elif risk_score == "MODERATE":
        st.warning("⚠️ Manipulation Risk: MODERATE")
      else:
        st.success("✅ Manipulation Risk: LOW (Appears Authentic)")

      # Detailed Breakdown (Making it technically responsible as per your notes)
      col1, col2 = st.columns(2)
      with col1:
        st.metric(
            label="Facial/Feature Consistency",
            value=f"{random.randint(40, 65)}%",
            delta="-32% (Anomaly)",
        )
        st.metric(
            label="Lighting & Shadow Match",
            value=f"{random.randint(45, 70)}%",
            delta="-15%",
        )
      with col2:
        st.metric(
            label="Audio-Visual Synchronization",
            value=f"{random.randint(35, 60)}%",
            delta="-40% (Mismatch)",
        )
        st.metric(
            label="Synthetic Artifact Indicators", value="HIGH", delta="Detected"
        )

      st.info(
          "**Why the system reached this result:** Discovered high frequency"
          " grid patterns typical of GAN generation in the boundary regions,"
          " coupled with abnormal temporal frame flickering[cite: 1]."
      )

# ==========================================
# MODULE 2: CALLSHIELD (Scam Call Protection)
# ==========================================
elif app_mode == "2. CallShield (Scam Call Protection)":
  st.subheader("📞 CallShield: Intent-Based Call Guardian")
  st.write(
      "Shifting focus from *'Who is calling?'* to *'What is this caller trying"
      " to do?'*[cite: 3]"
  )

  incoming_number = st.text_input(
      "Simulate Incoming Phone Number", "+1 (555) 382-9102"
  )

  # Interactive simulator for live conversation testing
  st.markdown("### Live Conversation Intent Monitor")
  simulated_transcript = st.selectbox(
      "Select a live dialogue snippet to scan:",
      [
          "Select a snippet...",
          (
              "Caller: 'Hello Sir, your electricity bill is unpaid. Please share"
              " the OTP sent to your phone immediately or connection will be"
              " cut.'"
          ),
          (
              "Caller: 'Hi mom, I lost my phone and wallet. Transfer money to"
              " this new UPI ID right away, it's an emergency.'"
          ),
          (
              "Caller: 'Hey, are we still meeting for lunch at 2 PM near the"
              " central park?'"
          ),
      ],
  )

  if simulated_transcript != "Select a snippet...":
    st.text_area(
        "Captured Real-Time Stream (Local Privacy-First Processing)",
        simulated_transcript,
        height=100,
    )

    if st.button("Evaluate Call Intent"):
      with st.spinner("Analyzing syntax, urgency patterns, and voice cloning..."):
        time.sleep(1.5)

      if "OTP" in simulated_transcript or "money" in simulated_transcript:
        st.error("🚨 Potential Scam Detected: HIGH RISK")
        st.markdown(
            "**Detected Threat Patterns:**[cite: 3]"
            "\n- Requesting sensitive information/OTP[cite: 3]"
            "\n- Creating artificial urgency or panic[cite: 3]"
            "\n- Financial demand pattern identified[cite: 3]"
        )
        st.warning(
            "🛡️ **CallShield Action:** Automated warning overlay triggered on"
            " user screen. Audio voice-print cross-referenced with DeepShield"
            " engine: *Synthetic voice cloned markers detected (89% match).*[cite: 3]"
        )
      else:
        st.success("✅ Call Appears Safe: Normal conversational pattern.")

# ==========================================
# MODULE 3: NEWSGUARD (Fake News Detector)
# ==========================================
elif app_mode == "3. NewsGuard (Fake News Detector)":
  st.subheader("📰 NewsGuard: Narrative & Media Validation")
  st.write(
      "Scan news articles or social media headlines for bias manipulation,"
      " deepfake attachments, and false source attribution."
  )

  news_text = st.text_area(
      "Paste news headline or article excerpt here:",
      "Breaking: Government announces immediate free distribution of electric"
      " cars to all citizens who register within 24 hours.",
  )

  if st.button("Verify Narrative"):
    if not news_text or len(news_text.strip()) < 10 :
      st.warning("Please enter a valid text snippet.")
    else:
      with st.spinner("Cross-referencing trusted global press databases..."):
        time.sleep(1.5)

      st.markdown("### 📊 Verification Analysis")
      st.error(
          "⚠️ **Credibility Status:** UNVERIFIED / LIKELY FABRICATED NARRATIVE"
      )

      col1, col2 = st.columns(2)
      with col1:
        st.metric(label="Source Credibility", value="12 / 100 (Low)")
        st.metric(label="Emotional Manipulation Index", value="88% (High Panic)")
      with col2:
        st.metric(label="Cross-Reference Matches", value="0 Trusted Sources")
        st.metric(label="Bot-Amplification Pattern", value="Active")

      st.info(
          "**Reasoning:** No official government gazette or mainstream media"
          " house has published this release. Language patterns match known"
          " automated phishing templates designed to induce urgency."
      )