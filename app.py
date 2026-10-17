import streamlit as st
import streamlit.components.v1 as components
from groq import Groq
import urllib.request
import json
import time
from datetime import datetime, timedelta

# ─── Page Configuration ───────────────────────────────────────────────────────
st.set_page_config(
    page_title="FreelanceShield OS",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─── ULTRA PREMIUM CSS ────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Space+Grotesk:wght@400;500;600;700&display=swap');

/* ══════════════════════════════════════════════
   DARK THEME NUKE — kill every Streamlit light bleed
   ══════════════════════════════════════════════ */

/* Top header / toolbar bar */
header[data-testid="stHeader"],
header[data-testid="stHeader"] > div,
.stAppHeader,
[data-testid="stAppViewBlockContainer"],
[data-testid="stToolbar"],
.stToolbar {
    background: #020817 !important;
    background-color: #020817 !important;
    border-bottom: 1px solid rgba(99,102,241,0.12) !important;
    box-shadow: 0 1px 20px -5px rgba(99,102,241,0.15) !important;
}

/* Every generic block / section Streamlit generates */
.block-container,
[data-testid="block-container"],
[data-testid="stVerticalBlock"],
[data-testid="stHorizontalBlock"],
[data-testid="stMainBlockContainer"],
[data-testid="stMain"],
[data-testid="stAppViewContainer"],
section.main,
.main > div,
.reportview-container,
.reportview-container .main {
    background: transparent !important;
    background-color: transparent !important;
}

/* Deploy button area */
[data-testid="stDecoration"],
[data-testid="stDecorationLine"] {
    background: linear-gradient(90deg, #6366f1, #8b5cf6) !important;
    height: 2px !important;
}

/* Modal / dialog overlays */
[data-testid="stModal"] > div,
div[role="dialog"],
div[data-baseweb="modal"],
div[data-baseweb="popover"] > div,
div[data-baseweb="tooltip"] > div {
    background: #0c0f1d !important;
    border: 1px solid rgba(99,102,241,0.25) !important;
    border-radius: 14px !important;
    color: #e2e8f0 !important;
}

/* Dropdown / select option lists */
div[data-baseweb="select"] > div,
div[data-baseweb="select"] ul,
div[data-baseweb="menu"],
[data-testid="stSelectboxVirtualDropdown"],
ul[data-testid="stSelectboxVirtualDropdown"] {
    background: #0c0f1d !important;
    border: 1px solid rgba(99,102,241,0.3) !important;
    border-radius: 10px !important;
}
div[data-baseweb="select"] li,
div[data-baseweb="menu"] li {
    background: transparent !important;
    color: #94a3b8 !important;
}
div[data-baseweb="select"] li:hover,
div[data-baseweb="menu"] li:hover,
div[data-baseweb="select"] [aria-selected="true"],
div[data-baseweb="menu"] [aria-selected="true"] {
    background: rgba(99,102,241,0.15) !important;
    color: #c7d2fe !important;
}

/* Notification / toast */
div[data-baseweb="notification"] {
    background: rgba(99,102,241,0.12) !important;
    border: 1px solid rgba(99,102,241,0.3) !important;
    border-radius: 10px !important;
    color: #c7d2fe !important;
}

/* Radio group backgrounds */
div[data-testid="stRadio"] > div {
    background: transparent !important;
}

/* Number input +/- buttons */
button[data-testid="stNumberInputStepDown"],
button[data-testid="stNumberInputStepUp"] {
    background: rgba(99,102,241,0.12) !important;
    border: 1px solid rgba(99,102,241,0.25) !important;
    color: #818cf8 !important;
    border-radius: 6px !important;
}
button[data-testid="stNumberInputStepDown"]:hover,
button[data-testid="stNumberInputStepUp"]:hover {
    background: rgba(99,102,241,0.25) !important;
}

/* Spinner overlay */
[data-testid="stSpinner"] {
    background: rgba(2,8,23,0.8) !important;
    backdrop-filter: blur(4px) !important;
}

/* Caption / small text */
small, .stCaption, [data-testid="stCaptionContainer"] {
    color: #4b5563 !important;
}

/* Divider */
hr, [data-testid="stSeparator"] {
    border-color: rgba(99,102,241,0.18) !important;
    background: rgba(99,102,241,0.18) !important;
}

/* ── Global Reset & Base ── */
*, *::before, *::after { box-sizing: border-box; }
html, body, [class*="css"], .stApp {
    font-family: 'Inter', 'Space Grotesk', sans-serif !important;
    background: #020817 !important;
}

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: #0d1526; }
::-webkit-scrollbar-thumb { background: linear-gradient(180deg,#6366f1,#8b5cf6); border-radius: 99px; }
::-webkit-scrollbar-thumb:hover { background: #818cf8; }

/* ── Main App Background ── */
.stApp {
    background: radial-gradient(ellipse 80% 50% at 50% -20%, rgba(99,102,241,0.15) 0%, transparent 60%),
                radial-gradient(ellipse 40% 30% at 80% 80%, rgba(139,92,246,0.08) 0%, transparent 50%),
                #020817 !important;
    min-height: 100vh;
}

/* ── Sidebar Premium Styling ── */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0c0f1d 0%, #0a0d1a 100%) !important;
    border-right: 1px solid rgba(99,102,241,0.2) !important;
    box-shadow: 4px 0 30px -5px rgba(99,102,241,0.15) !important;
}
[data-testid="stSidebar"]::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, #6366f1, #8b5cf6, #06b6d4, #6366f1);
    background-size: 200% 100%;
    animation: shimmer 3s linear infinite;
}
[data-testid="stSidebar"] .stMarkdown h2 {
    color: #e2e8f0 !important;
    font-weight: 700 !important;
    font-size: 0.95rem !important;
    letter-spacing: 0.5px !important;
    text-transform: uppercase !important;
    opacity: 0.9 !important;
}
[data-testid="stSidebar"] label {
    color: #94a3b8 !important;
    font-size: 0.82rem !important;
    font-weight: 500 !important;
}
[data-testid="stSidebar"] .stSelectbox > div > div,
[data-testid="stSidebar"] .stTextInput > div > div > input,
[data-testid="stSidebar"] .stNumberInput > div > div > input {
    background: rgba(15,23,42,0.9) !important;
    border: 1px solid rgba(99,102,241,0.3) !important;
    color: #e2e8f0 !important;
    border-radius: 8px !important;
    transition: border-color 0.2s ease, box-shadow 0.2s ease !important;
}
[data-testid="stSidebar"] .stSelectbox > div > div:hover,
[data-testid="stSidebar"] .stTextInput > div > div > input:focus,
[data-testid="stSidebar"] .stNumberInput > div > div > input:focus {
    border-color: rgba(99,102,241,0.6) !important;
    box-shadow: 0 0 0 3px rgba(99,102,241,0.15) !important;
}

/* ── Info box in sidebar ── */
[data-testid="stSidebar"] .stAlert {
    background: rgba(99,102,241,0.1) !important;
    border: 1px solid rgba(99,102,241,0.3) !important;
    border-radius: 10px !important;
    color: #c7d2fe !important;
}

/* ── Divider ── */
hr { border-color: rgba(99,102,241,0.2) !important; }

/* ── Checkbox styling ── */
[data-testid="stSidebar"] .stCheckbox label { color: #94a3b8 !important; font-size: 0.85rem !important; }
[data-testid="stSidebar"] .stCheckbox input:checked + div { background: #6366f1 !important; }

/* ── Radio ── */
[data-testid="stSidebar"] .stRadio label { color: #94a3b8 !important; font-size: 0.85rem !important; }
[data-testid="stSidebar"] .stRadio div[data-checked="true"] { color: #818cf8 !important; }

/* ── Slider ── */
[data-testid="stSidebar"] .stSlider > div > div > div {
    background: linear-gradient(90deg, #6366f1, #8b5cf6) !important;
}

/* ── Main content inputs ── */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea {
    background: rgba(15,23,42,0.8) !important;
    border: 1px solid rgba(99,102,241,0.25) !important;
    color: #e2e8f0 !important;
    border-radius: 10px !important;
    font-family: 'Inter', sans-serif !important;
    transition: all 0.2s ease !important;
    padding: 10px 14px !important;
}
.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {
    border-color: rgba(99,102,241,0.6) !important;
    box-shadow: 0 0 0 3px rgba(99,102,241,0.15), 0 0 20px -5px rgba(99,102,241,0.3) !important;
    outline: none !important;
}
.stTextInput > div > div > input::placeholder,
.stTextArea > div > div > textarea::placeholder { color: rgba(148,163,184,0.5) !important; }

/* Input label */
.stTextInput label, .stTextArea label, .stSelectbox label, .stNumberInput label { 
    color: #94a3b8 !important; 
    font-size: 0.82rem !important; 
    font-weight: 600 !important;
    letter-spacing: 0.3px !important;
    text-transform: uppercase !important;
}

/* ── Select slider ── */
.stSelectSlider > div { color: #e2e8f0 !important; }
.stSelectSlider > div > div { background: rgba(15,23,42,0.8) !important; border: 1px solid rgba(99,102,241,0.25) !important; border-radius: 8px !important; }

/* ── Primary Button ── */
.stButton > button[kind="primary"],
.stButton > button[data-testid="baseButton-primary"] {
    background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%) !important;
    border: none !important;
    color: white !important;
    font-weight: 700 !important;
    font-size: 0.95rem !important;
    letter-spacing: 0.3px !important;
    border-radius: 12px !important;
    padding: 14px 24px !important;
    box-shadow: 0 4px 20px -5px rgba(99,102,241,0.6), 0 0 40px -15px rgba(139,92,246,0.4) !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    position: relative !important;
    overflow: hidden !important;
}
.stButton > button[kind="primary"]:hover,
.stButton > button[data-testid="baseButton-primary"]:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 30px -5px rgba(99,102,241,0.7), 0 0 60px -10px rgba(139,92,246,0.5) !important;
    background: linear-gradient(135deg, #818cf8 0%, #a78bfa 100%) !important;
}
.stButton > button[kind="primary"]:active,
.stButton > button[data-testid="baseButton-primary"]:active {
    transform: translateY(0px) !important;
}

/* ── Secondary Buttons ── */
.stButton > button[kind="secondary"],
.stButton > button[data-testid="baseButton-secondary"] {
    background: rgba(15,23,42,0.8) !important;
    border: 1px solid rgba(99,102,241,0.35) !important;
    color: #c7d2fe !important;
    font-weight: 600 !important;
    border-radius: 10px !important;
    transition: all 0.25s ease !important;
    backdrop-filter: blur(8px) !important;
}
.stButton > button[kind="secondary"]:hover,
.stButton > button[data-testid="baseButton-secondary"]:hover {
    background: rgba(99,102,241,0.15) !important;
    border-color: rgba(99,102,241,0.6) !important;
    color: #818cf8 !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 4px 15px -5px rgba(99,102,241,0.3) !important;
}

/* ── Download Button ── */
.stDownloadButton > button {
    background: rgba(16,185,129,0.1) !important;
    border: 1px solid rgba(16,185,129,0.4) !important;
    color: #34d399 !important;
    font-weight: 600 !important;
    border-radius: 10px !important;
    transition: all 0.25s ease !important;
}
.stDownloadButton > button:hover {
    background: rgba(16,185,129,0.2) !important;
    border-color: rgba(52,211,153,0.6) !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 4px 15px -5px rgba(16,185,129,0.3) !important;
}

/* ── TABS ── */
.stTabs [data-baseweb="tab-list"] {
    background: rgba(10,13,26,0.8) !important;
    border-radius: 12px !important;
    padding: 5px !important;
    gap: 4px !important;
    border: 1px solid rgba(99,102,241,0.15) !important;
    backdrop-filter: blur(10px) !important;
}
.stTabs [data-baseweb="tab"] {
    border-radius: 8px !important;
    font-weight: 600 !important;
    font-size: 0.85rem !important;
    color: #64748b !important;
    padding: 8px 16px !important;
    transition: all 0.2s ease !important;
    background: transparent !important;
    border: none !important;
}
.stTabs [data-baseweb="tab"]:hover {
    color: #94a3b8 !important;
    background: rgba(99,102,241,0.08) !important;
}
.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, rgba(99,102,241,0.25), rgba(139,92,246,0.2)) !important;
    color: #a5b4fc !important;
    box-shadow: 0 0 20px -5px rgba(99,102,241,0.3), inset 0 1px 0 rgba(255,255,255,0.05) !important;
}
.stTabs [data-baseweb="tab-panel"] {
    padding-top: 20px !important;
}

/* ── Alerts / Info ── */
.stAlert {
    border-radius: 12px !important;
    border: none !important;
    backdrop-filter: blur(8px) !important;
}
.stAlert[data-baseweb="notification"] {
    background: rgba(99,102,241,0.1) !important;
    border: 1px solid rgba(99,102,241,0.3) !important;
    color: #c7d2fe !important;
}

/* ── Spinner ── */
.stSpinner > div { border-top-color: #6366f1 !important; }

/* ── Markdown Headings ── */
.stMarkdown h3 {
    color: #e2e8f0 !important;
    font-weight: 700 !important;
    font-size: 1.05rem !important;
    letter-spacing: -0.3px !important;
    margin-bottom: 12px !important;
}
.stMarkdown h4 {
    color: #cbd5e1 !important;
    font-weight: 600 !important;
}
.stMarkdown p { color: #94a3b8 !important; line-height: 1.7 !important; }
.stMarkdown strong { color: #e2e8f0 !important; }
.stMarkdown li { color: #94a3b8 !important; }
.stMarkdown a { color: #818cf8 !important; }
.stMarkdown hr { border-color: rgba(99,102,241,0.2) !important; }

/* ── Success message ── */
.stSuccess {
    background: rgba(16,185,129,0.1) !important;
    border: 1px solid rgba(52,211,153,0.3) !important;
    border-radius: 10px !important;
    color: #6ee7b7 !important;
}

/* ── Error message ── */
.stError {
    background: rgba(239,68,68,0.1) !important;
    border: 1px solid rgba(239,68,68,0.3) !important;
    border-radius: 10px !important;
}

/* ── Caption ── */
.stCaption { color: #4b5563 !important; font-size: 0.8rem !important; }

/* ── Select box arrow ── */
.stSelectbox svg { color: #6366f1 !important; }

/* ── Animations ── */
@keyframes shimmer {
    0% { background-position: -200% 0; }
    100% { background-position: 200% 0; }
}
@keyframes float {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-6px); }
}
@keyframes pulse-glow {
    0%, 100% { box-shadow: 0 0 20px -5px rgba(99,102,241,0.4); }
    50% { box-shadow: 0 0 40px -5px rgba(99,102,241,0.7), 0 0 60px -10px rgba(139,92,246,0.4); }
}
@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}
@keyframes slideInRight {
    from { opacity: 0; transform: translateX(-15px); }
    to { opacity: 1; transform: translateX(0); }
}
@keyframes scanline {
    0% { top: 0%; }
    100% { top: 100%; }
}
@keyframes borderRotate {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* ── HERO BOX ── */
.hero-box {
    background:
        radial-gradient(circle at 20% 50%, rgba(99,102,241,0.18) 0%, transparent 50%),
        radial-gradient(circle at 80% 20%, rgba(139,92,246,0.12) 0%, transparent 40%),
        radial-gradient(circle at 50% 100%, rgba(6,182,212,0.08) 0%, transparent 50%),
        linear-gradient(135deg, #080d1f 0%, #0c1128 50%, #07091a 100%);
    padding: 36px 40px;
    border-radius: 20px;
    color: white;
    margin-bottom: 28px;
    position: relative;
    overflow: hidden;
    animation: fadeInUp 0.6s ease both;
}
.hero-box::before {
    content: '';
    position: absolute;
    inset: 0;
    border-radius: 20px;
    padding: 1.5px;
    background: linear-gradient(135deg, rgba(99,102,241,0.6), rgba(139,92,246,0.4), rgba(6,182,212,0.3), rgba(99,102,241,0.6));
    background-size: 200% 200%;
    animation: borderRotate 4s ease infinite;
    -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
    -webkit-mask-composite: xor;
    mask-composite: exclude;
}
.hero-box::after {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 3px;
    background: linear-gradient(90deg, transparent, rgba(99,102,241,0.5), rgba(139,92,246,0.5), transparent);
    animation: scanline 4s linear infinite;
    opacity: 0.6;
}
.hero-grid {
    display: grid;
    grid-template-columns: 1fr auto;
    gap: 24px;
    align-items: center;
}
.hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: linear-gradient(90deg, rgba(16,185,129,0.15), rgba(6,182,212,0.15));
    color: #6ee7b7;
    padding: 5px 14px 5px 10px;
    border-radius: 999px;
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.8px;
    border: 1px solid rgba(110,231,183,0.3);
    margin-bottom: 14px;
    text-transform: uppercase;
}
.hero-badge-dot {
    width: 7px; height: 7px;
    background: #34d399;
    border-radius: 50%;
    animation: pulse-glow 2s ease infinite;
    box-shadow: 0 0 8px rgba(52,211,153,0.8);
}
.hero-title {
    margin: 0 0 10px 0;
    font-size: 2.6rem;
    font-weight: 900;
    color: white;
    letter-spacing: -1px;
    line-height: 1.1;
    font-family: 'Space Grotesk', sans-serif;
}
.hero-title-accent { 
    background: linear-gradient(135deg, #818cf8, #a78bfa, #67e8f9);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.hero-desc {
    margin: 0;
    color: rgba(203,213,225,0.85);
    font-size: 1rem;
    max-width: 680px;
    line-height: 1.65;
}
.hero-desc b { color: #e2e8f0; }
.hero-stats {
    display: flex;
    flex-direction: column;
    gap: 12px;
    align-items: flex-end;
}
.hero-stat-pill {
    background: rgba(99,102,241,0.12);
    border: 1px solid rgba(99,102,241,0.25);
    border-radius: 10px;
    padding: 10px 16px;
    text-align: right;
    min-width: 140px;
}
.hero-stat-val { font-size: 1.5rem; font-weight: 800; color: #818cf8; font-family: 'Space Grotesk', sans-serif; }
.hero-stat-lbl { font-size: 0.7rem; color: #64748b; text-transform: uppercase; letter-spacing: 0.5px; font-weight: 600; }

/* ── METRIC CARDS ── */
.metrics-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 12px;
    margin-bottom: 22px;
    animation: fadeInUp 0.5s ease 0.1s both;
}
.metric-card {
    background: rgba(15,23,42,0.7);
    border: 1px solid rgba(99,102,241,0.2);
    padding: 16px 18px;
    border-radius: 14px;
    text-align: center;
    position: relative;
    overflow: hidden;
    transition: all 0.3s ease;
    backdrop-filter: blur(10px);
}
.metric-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: var(--card-accent, linear-gradient(90deg, #6366f1, #8b5cf6));
}
.metric-card:hover {
    transform: translateY(-3px);
    border-color: rgba(99,102,241,0.4);
    box-shadow: 0 8px 30px -10px rgba(99,102,241,0.3);
}
.metric-val {
    font-size: 1.45rem;
    font-weight: 800;
    color: #38bdf8;
    margin: 6px 0 4px;
    font-family: 'Space Grotesk', sans-serif;
    letter-spacing: -0.5px;
}
.metric-lbl {
    font-size: 0.7rem;
    color: #4b5563;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    font-weight: 600;
}
.metric-icon {
    font-size: 1.3rem;
    margin-bottom: 2px;
    display: block;
}

/* ── SCENARIO BUTTONS ── */
.scenario-section {
    margin-bottom: 24px;
}
.section-label {
    font-size: 0.72rem;
    font-weight: 700;
    color: #4b5563;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 10px;
    display: flex;
    align-items: center;
    gap: 8px;
}
.section-label::after {
    content: '';
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, rgba(99,102,241,0.3), transparent);
}

/* ── WORKSPACE CARD ── */
.workspace-card {
    background: rgba(10,13,26,0.6);
    border: 1px solid rgba(99,102,241,0.15);
    border-radius: 16px;
    padding: 24px;
    backdrop-filter: blur(12px);
    animation: fadeInUp 0.6s ease 0.15s both;
}
.workspace-empty {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 320px;
    text-align: center;
    padding: 40px;
}
.workspace-empty-icon {
    font-size: 4rem;
    margin-bottom: 16px;
    animation: float 3s ease infinite;
    filter: drop-shadow(0 0 20px rgba(99,102,241,0.4));
}
.workspace-empty-title {
    font-size: 1.25rem;
    font-weight: 700;
    color: #e2e8f0;
    margin-bottom: 8px;
    font-family: 'Space Grotesk', sans-serif;
}
.workspace-empty-sub {
    color: #4b5563;
    font-size: 0.9rem;
    max-width: 360px;
    line-height: 1.6;
}
.workspace-step {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    background: rgba(99,102,241,0.1);
    border: 1px solid rgba(99,102,241,0.2);
    border-radius: 10px;
    padding: 10px 16px;
    margin: 6px 0;
    width: 100%;
    max-width: 400px;
    text-align: left;
    color: #64748b;
    font-size: 0.88rem;
}
.workspace-step-num {
    width: 24px; height: 24px;
    background: linear-gradient(135deg, #6366f1, #8b5cf6);
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 0.72rem;
    font-weight: 800;
    color: white;
    flex-shrink: 0;
}

/* ── INPUT SECTION ── */
.input-card {
    background: rgba(10,13,26,0.5);
    border: 1px solid rgba(99,102,241,0.12);
    border-radius: 16px;
    padding: 20px;
    margin-bottom: 16px;
    backdrop-filter: blur(8px);
    animation: fadeInUp 0.5s ease both;
}

/* ── SIDEBAR SECTION HEADER ── */
.sidebar-section-header {
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 6px 0;
    margin-bottom: 10px;
    font-size: 0.8rem;
    font-weight: 700;
    color: #6366f1;
    text-transform: uppercase;
    letter-spacing: 0.8px;
}
.sidebar-section-header::before {
    content: '';
    display: block;
    width: 3px;
    height: 16px;
    background: linear-gradient(180deg, #6366f1, #8b5cf6);
    border-radius: 2px;
}

/* ── RESULT CONTENT ── */
.tab-content-wrapper {
    color: #cbd5e1;
    line-height: 1.8;
}
.tab-content-wrapper h1, .tab-content-wrapper h2 { color: #e2e8f0 !important; font-family: 'Space Grotesk', sans-serif !important; }
.tab-content-wrapper h3 { color: #c7d2fe !important; }
.tab-content-wrapper table {
    border-collapse: collapse !important;
    width: 100% !important;
    border-radius: 8px !important;
    overflow: hidden !important;
}
.tab-content-wrapper th {
    background: rgba(99,102,241,0.2) !important;
    color: #a5b4fc !important;
    padding: 10px 14px !important;
    font-size: 0.82rem !important;
    text-transform: uppercase !important;
    letter-spacing: 0.5px !important;
}
.tab-content-wrapper td {
    padding: 10px 14px !important;
    border-bottom: 1px solid rgba(99,102,241,0.1) !important;
    color: #94a3b8 !important;
}
.tab-content-wrapper blockquote {
    border-left: 3px solid #6366f1 !important;
    background: rgba(99,102,241,0.08) !important;
    padding: 12px 16px !important;
    border-radius: 0 8px 8px 0 !important;
    color: #a5b4fc !important;
}
.tab-content-wrapper code {
    background: rgba(99,102,241,0.15) !important;
    color: #a5b4fc !important;
    padding: 2px 6px !important;
    border-radius: 4px !important;
    font-size: 0.85em !important;
}

/* ── RISK SCORE DISPLAY ── */
.risk-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: rgba(15,23,42,0.7);
    border: 1px solid rgba(99,102,241,0.2);
    border-radius: 14px;
    padding: 20px 24px;
    margin-bottom: 20px;
}

/* ── SECTION NUMBERS ── */
.section-num {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    font-size: 0.8rem;
    font-weight: 700;
    color: #6366f1;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    margin-bottom: 12px;
}
.section-num-badge {
    width: 22px; height: 22px;
    background: linear-gradient(135deg, #6366f1, #8b5cf6);
    border-radius: 6px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-size: 0.7rem;
    font-weight: 800;
    color: white;
}

/* ── GENERATE BUTTON WRAPPER ── */
.generate-btn-wrapper {
    margin-top: 8px;
}

/* ── Number input ── */
.stNumberInput > div > div > input {
    background: rgba(15,23,42,0.8) !important;
    border: 1px solid rgba(99,102,241,0.25) !important;
    color: #e2e8f0 !important;
    border-radius: 8px !important;
}

/* ── Select box main ── */
.stSelectbox > div > div {
    background: rgba(15,23,42,0.8) !important;
    border: 1px solid rgba(99,102,241,0.25) !important;
    color: #e2e8f0 !important;
    border-radius: 10px !important;
}

/* ── Select box option ── */
[data-testid="stSelectbox"] option { background: #0c0f1d !important; }

/* ── Tooltip ── */
.stTooltipIcon { color: #6366f1 !important; }

</style>
""", unsafe_allow_html=True)

# ─── HERO SECTION ─────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-box">
    <div class="hero-grid">
        <div>
            <div class="hero-badge">
                <div class="hero-badge-dot"></div>
                Open-Weight AI Micro-SaaS &nbsp;·&nbsp; Groq Cloud &amp; Local Ollama Ready
            </div>
            <h1 class="hero-title">
                🛡️ FreelanceShield <span class="hero-title-accent">OS</span>
            </h1>
            <p class="hero-desc">
                Stop losing money to <b>"bhai ek chota sa change aur kar do"</b>. Convert messy client chats into ironclad
                <b>Legal Contracts, Printable Tax Invoices, WhatsApp Pitches &amp; Anti-Scope-Creep Replies</b> — in 1.5 seconds.
            </p>
        </div>
        <div class="hero-stats">
            <div class="hero-stat-pill">
                <div class="hero-stat-val">⚡ 1.5s</div>
                <div class="hero-stat-lbl">Generation Speed</div>
            </div>
            <div class="hero-stat-pill">
                <div class="hero-stat-val" style="color:#34d399;">0%</div>
                <div class="hero-stat-lbl">API Lock-In</div>
            </div>
            <div class="hero-stat-pill">
                <div class="hero-stat-val" style="color:#f59e0b;">4-in-1</div>
                <div class="hero-stat-lbl">Output Suite</div>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ─── Initialize Session State ─────────────────────────────────────────────────
defaults = {
    "raw_notes": "",
    "freelancer": "",
    "client": "",
    "amount": 6000,
    "generated": False,
    "contract_md": "",
    "pitch_md": "",
    "risk_md": "",
    "elapsed": 0.0,
    "used_model": ""
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

# ─── Helper: AI Call ──────────────────────────────────────────────────────────
def run_open_ai(provider, api_key, ollama_url, model_name, system_prompt, user_prompt):
    if provider.startswith("☁️ Groq"):
        client = Groq(api_key=api_key)
        resp = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.35,
        )
        return resp.choices[0].message.content
    else:
        url = f"{ollama_url.rstrip('/')}/api/chat"
        payload = {
            "model": model_name,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            "stream": False
        }
        req = urllib.request.Request(
            url,
            data=json.dumps(payload).encode('utf-8'),
            headers={'Content-Type': 'application/json'}
        )
        with urllib.request.urlopen(req) as response:
            res_data = json.loads(response.read().decode('utf-8'))
            return res_data["message"]["content"]

# ─── SIDEBAR ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown('<div class="sidebar-section-header">🧠 &nbsp;AI Engine</div>', unsafe_allow_html=True)
    provider = st.radio(
        "Inference Mode:",
        ["☁️ Groq Open-Weight Cloud", "🏠 Local Ollama (100% Offline)"],
        help="Run via ultra-fast Groq LPUs or 100% offline on your laptop using Ollama!"
    )

    api_key = ""
    ollama_url = "http://localhost:11434"

    if provider.startswith("☁️ Groq"):
        api_key = st.text_input("🔑 Groq API Key (gsk_...):", type="password")
        available_models = ["llama-3.1-8b-instant", "llama3-8b-8192", "mixtral-8x7b-32768", "gemma2-9b-it"]
        if api_key:
            try:
                temp_client = Groq(api_key=api_key)
                models_data = temp_client.models.list()
                fetched = [
                    m.id for m in models_data.data
                    if not any(x in m.id.lower() for x in ["whisper", "guard", "tts", "vision"])
                ]
                if fetched:
                    available_models = sorted(fetched, reverse=True)
            except Exception:
                pass
        model_choice = st.selectbox("Select Open-Weight Model:", available_models)
    else:
        ollama_url = st.text_input("🔌 Ollama URL:", value="http://localhost:11434")
        model_choice = st.text_input("🦙 Local Model Name:", value="llama3.2")
        st.caption("💡 100% offline. Zero data leaves your machine!")

    st.divider()

    st.markdown('<div class="sidebar-section-header">💰 &nbsp;Deal Calculator</div>', unsafe_allow_html=True)
    currency_map = {"₹ INR": "₹", "$ USD": "$", "€ EUR": "€", "£ GBP": "£"}
    currency_label = st.selectbox("Currency:", list(currency_map.keys()))
    sym = currency_map[currency_label]

    total_fee = st.number_input(f"Total Project Fee ({sym}):", min_value=100, value=int(st.session_state.amount), step=500)
    upfront_pct = st.slider("Upfront Advance (%):", 0, 100, 50, 5)
    tax_pct = st.slider("GST / Tax (%):", 0, 28, 0, 2)

    tax_amt = round(total_fee * (tax_pct / 100))
    grand_total = total_fee + tax_amt
    upfront_amt = round(grand_total * (upfront_pct / 100))
    balance_amt = grand_total - upfront_amt

    st.markdown(f"""
    <div style="background: linear-gradient(135deg, rgba(99,102,241,0.08), rgba(16,185,129,0.06));
                border: 1px solid rgba(99,102,241,0.25); border-radius: 12px; padding: 16px; margin-top: 8px;">
        <div style="font-size: 0.72rem; color: #6366f1; font-weight: 700; text-transform: uppercase; letter-spacing: 0.8px; margin-bottom: 10px;">🧾 Auto Split</div>
        <div style="display: flex; justify-content: space-between; margin-bottom: 6px; font-size: 0.85rem;">
            <span style="color: #64748b;">Total + Tax</span>
            <span style="color: #e2e8f0; font-weight: 700;">{sym}{grand_total:,}</span>
        </div>
        <div style="display: flex; justify-content: space-between; margin-bottom: 6px; font-size: 0.85rem;">
            <span style="color: #64748b;">Upfront ({upfront_pct}%)</span>
            <span style="color: #34d399; font-weight: 700;">{sym}{upfront_amt:,}</span>
        </div>
        <div style="display: flex; justify-content: space-between; font-size: 0.85rem; padding-top: 8px; border-top: 1px solid rgba(99,102,241,0.2);">
            <span style="color: #64748b;">On Delivery</span>
            <span style="color: #f59e0b; font-weight: 700;">{sym}{balance_amt:,}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    st.markdown('<div class="sidebar-section-header">🛡️ &nbsp;Legal Guardrails</div>', unsafe_allow_html=True)
    free_revisions = st.number_input("Included Free Revisions:", 0, 10, 2)
    extra_rev_cost = st.number_input(f"Cost per Extra Revision ({sym}):", 0, 10000, 500, step=100)
    late_fee = st.checkbox("5% Weekly Late Payment Penalty", value=True)
    ip_lock = st.checkbox("Retain IP Rights Until 100% Paid", value=True)
    kill_clause = st.checkbox("Non-Refundable Kill Fee on Cancellation", value=True)

# ─── MAIN LAYOUT ──────────────────────────────────────────────────────────────
col1, col2 = st.columns([1.0, 1.35], gap="large")

with col1:
    # ── Quick-Load Scenarios ──
    st.markdown("""
    <div class="section-num">
        <span class="section-num-badge">1</span>
        Quick-Load Real Scenarios
    </div>
    """, unsafe_allow_html=True)

    p1, p2, p3 = st.columns(3)
    with p1:
        if st.button("🎬 Reels Editor", use_container_width=True):
            st.session_state.freelancer = "Aarav Visuals Studio"
            st.session_state.client = "FitLife Gym & Cafe"
            st.session_state.amount = 6000
            st.session_state.raw_notes = "Client ko 6 Instagram Reels aur 2 YouTube Shorts edit karwane hain (captions, B-roll, sound effects ke saath). Delivery 5 din me deni hai. Raw footage client Google Drive pe dega. Music copyright ki zimmedari client ki hogi."
            st.rerun()
    with p2:
        if st.button("💻 Full-Stack Dev", use_container_width=True):
            st.session_state.freelancer = "DevCraft Labs"
            st.session_state.client = "UrbanTrendz E-Com"
            st.session_state.amount = 25000
            st.session_state.raw_notes = "5-page responsive e-commerce landing website with Razorpay payment gateway integration. Timeline 10 days. Domain, hosting, aur paid plugins ka kharcha client dega. Deployment ke baad 7 din free bug support milega, uske baad naye features alag se charge honge."
            st.rerun()
    with p3:
        if st.button("🎨 Brand Designer", use_container_width=True):
            st.session_state.freelancer = "PixelPulse Creative"
            st.session_state.client = "BrewHaHa Roasters"
            st.session_state.amount = 12000
            st.session_state.raw_notes = "Primary Logo design + 3 coffee pouch packaging mockups + brand color guide chahiye. Timeline 7 days. Shuru me 3 logo concepts dikhaunga jisme se 1 final hoga. Open source files (.AI / .PSD) full payment ke baad hi share hongi."
            st.rerun()

    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

    # ── Project Details ──
    st.markdown("""
    <div class="section-num">
        <span class="section-num-badge">2</span>
        Project &amp; Client Details
    </div>
    """, unsafe_allow_html=True)

    c_a, c_b = st.columns(2)
    with c_a:
        freelancer_name = st.text_input(
            "Your Name / Agency:",
            value=st.session_state.freelancer,
            placeholder="e.g., Rahul Sharma Studio"
        )
    with c_b:
        client_name = st.text_input(
            "Client / Brand Name:",
            value=st.session_state.client,
            placeholder="e.g., TechNova Pvt Ltd"
        )

    raw_notes = st.text_area(
        "Paste Messy Client Chat or Rough Notes (Hinglish / English):",
        value=st.session_state.raw_notes,
        height=140,
        placeholder="e.g., Client ko 5 reels chahiye 5000 me, 4 din me dena hai..."
    )

    strictness = st.select_slider(
        "⚖️ Contract Tone & Strictness:",
        options=["Friendly & Warm", "Balanced Corporate", "Ironclad & Strict"],
        value="Balanced Corporate"
    )

    st.markdown("<div style='height: 6px;'></div>", unsafe_allow_html=True)
    generate_btn = st.button("🚀  Generate Complete Protection Suite", type="primary", use_container_width=True)

    # ── Tone indicator ──
    tone_colors = {
        "Friendly & Warm": ("#34d399", "Relaxed, trust-first approach"),
        "Balanced Corporate": ("#f59e0b", "Professional, balanced protection"),
        "Ironclad & Strict": ("#f87171", "Maximum legal protection, zero ambiguity"),
    }
    t_color, t_desc = tone_colors[strictness]
    st.markdown(f"""
    <div style="display: flex; align-items: center; gap: 10px; padding: 10px 14px;
                background: rgba(15,23,42,0.5); border: 1px solid rgba(99,102,241,0.12);
                border-radius: 8px; margin-top: 8px;">
        <div style="width: 8px; height: 8px; border-radius: 50%; background: {t_color}; flex-shrink: 0;
                    box-shadow: 0 0 8px {t_color}88;"></div>
        <span style="font-size: 0.8rem; color: #64748b;">{t_desc}</span>
    </div>
    """, unsafe_allow_html=True)

    # ── Generation Logic ──
    if generate_btn:
        if provider.startswith("☁️ Groq") and not api_key:
            st.error("⚠️ Bhai, left sidebar me apni Groq API Key (`gsk_...`) paste kar!")
        elif not raw_notes.strip():
            st.warning("⚠️ Upar koi Demo button daba ya project details likh!")
        else:
            try:
                start_t = time.time()
                with st.spinner(f"⚡ Crafting legal suite via `{model_choice}`..."):
                    guardrails = [
                        f"Maximum {free_revisions} free revision rounds included; additional revisions billed at {sym}{extra_rev_cost} per request.",
                        f"Total Project Fee: {sym}{total_fee:,} + {tax_pct}% Tax = {sym}{grand_total:,}.",
                        f"Payment Schedule: {upfront_pct}% upfront ({sym}{upfront_amt:,}) before kickoff, and {100-upfront_pct}% ({sym}{balance_amt:,}) upon final completion."
                    ]
                    if late_fee:
                        guardrails.append("5% weekly late payment penalty applies to overdue invoices.")
                    if ip_lock:
                        guardrails.append("Intellectual Property (IP) and editable source files remain the Freelancer's property until 100% payment is received.")
                    if kill_clause:
                        guardrails.append("Upfront deposit is a non-refundable booking/kill fee if the client cancels mid-project.")

                    sys_msg = "You are an elite legal counsel and business strategist for independent freelancers. Always separate the 3 requested sections strictly with ===SPLIT===."
                    usr_msg = f"""
                    Convert the following raw project notes (which may be in Hinglish or English) into a 3-part business protection suite separated strictly by `===SPLIT===`.

                    Freelancer: {freelancer_name or 'Independent Contractor'}
                    Client: {client_name or 'Client'}
                    Tone: {strictness}
                    Mandatory Financial & Legal Guardrails: {" | ".join(guardrails)}
                    Raw Notes: {raw_notes}

                    Produce EXACTLY 3 sections separated by `===SPLIT===`:

                    SECTION 1: **Official Scope of Work (SoW) & Micro-Contract** in clean Markdown. Include:
                    - Project Summary & Explicit Deliverables
                    - Strict "Out-of-Scope" Boundaries (Anti-Scope Creep)
                    - Revision Policy ({free_revisions} free, {sym}{extra_rev_cost}/extra)
                    - Timeline & Delivery Terms
                    - Payment Schedule ({sym}{upfront_amt:,} upfront, {sym}{balance_amt:,} on completion)
                    - Legal Protection Clauses & Sign-Off Block

                    ===SPLIT===

                    SECTION 2: **Client Onboarding Messages**:
                    1. **WhatsApp / Instagram DM Pitch**: Friendly, confident message summarizing deliverables, upfront deposit ({sym}{upfront_amt:,}), and asking for a quick "Approved 👍" reply.
                    2. **Hinglish WhatsApp Version**: Natural professional Hinglish message for Indian clients so it doesn't feel overly robotic.
                    3. **Formal Email Version**: Clean corporate email template.

                    ===SPLIT===

                    SECTION 3: **🚨 Red Flag & Scope Creep Vulnerability Audit**:
                    - **Deal Safety Score**: X / 100
                    - **Hidden Loopholes in Client Notes**: 3 specific things left vague that could cause disputes.
                    - **Pre-Emptive Advice**: Actionable tips for the freelancer before starting work.
                    """

                    output_text = run_open_ai(provider, api_key, ollama_url, model_choice, sys_msg, usr_msg)
                    parts = output_text.split("===SPLIT===")

                    st.session_state.contract_md = parts[0].strip() if len(parts) > 0 else output_text
                    st.session_state.pitch_md = parts[1].strip() if len(parts) > 1 else "See main contract tab."
                    st.session_state.risk_md = parts[2].strip() if len(parts) > 2 else "See main contract tab."
                    st.session_state.elapsed = round(time.time() - start_t, 2)
                    st.session_state.used_model = model_choice
                    st.session_state.generated = True
            except Exception as e:
                st.error(f"Error: {e}")


# ─── RIGHT COLUMN: WORKSPACE ──────────────────────────────────────────────────
with col2:
    st.markdown("""
    <div class="section-num" style="margin-bottom: 16px;">
        <span class="section-num-badge">3</span>
        AI Business Protection Workspace
    </div>
    """, unsafe_allow_html=True)

    if st.session_state.generated:
        # ── Metric Cards ──
        st.markdown(f"""
        <div class="metrics-grid">
            <div class="metric-card" style="--card-accent: linear-gradient(90deg, #6366f1, #8b5cf6);">
                <span class="metric-icon">⚡</span>
                <div class="metric-val">{st.session_state.elapsed}s</div>
                <div class="metric-lbl">Latency</div>
            </div>
            <div class="metric-card" style="--card-accent: linear-gradient(90deg, #8b5cf6, #a78bfa);">
                <span class="metric-icon">🧠</span>
                <div class="metric-val" style="font-size: 0.9rem; color: #a78bfa;">{st.session_state.used_model[:18]}</div>
                <div class="metric-lbl">Model Used</div>
            </div>
            <div class="metric-card" style="--card-accent: linear-gradient(90deg, #10b981, #34d399);">
                <span class="metric-icon">💰</span>
                <div class="metric-val" style="color: #34d399;">{sym}{grand_total:,}</div>
                <div class="metric-lbl">Deal Value</div>
            </div>
            <div class="metric-card" style="--card-accent: linear-gradient(90deg, #f59e0b, #fbbf24);">
                <span class="metric-icon">🔓</span>
                <div class="metric-val" style="color: #fbbf24; font-size: 1rem;">Open Source</div>
                <div class="metric-lbl">0% Lock-In</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # ── Tabs ──
        tab1, tab2, tab3, tab4 = st.tabs([
            "📄  Legal Contract",
            "🧾  Invoice & PDF",
            "💬  WhatsApp Pitches",
            "🥊  Scope-Creep Shield"
        ])

        with tab1:
            st.markdown('<div class="tab-content-wrapper">', unsafe_allow_html=True)
            st.markdown(st.session_state.contract_md)
            st.markdown('</div>', unsafe_allow_html=True)
            st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)
            st.download_button(
                "📥  Download Contract (.md)",
                data=st.session_state.contract_md,
                file_name=f"SoW_{(client_name or 'Client').replace(' ', '_')}.md",
                mime="text/markdown",
                use_container_width=True
            )

        with tab2:
            st.markdown("""
            <div style="display: flex; align-items: center; gap: 10px; padding: 12px 16px;
                        background: rgba(6,182,212,0.08); border: 1px solid rgba(6,182,212,0.25);
                        border-radius: 10px; margin-bottom: 16px;">
                <span style="font-size: 1.2rem;">💡</span>
                <span style="font-size: 0.85rem; color: #67e8f9;">
                    Click <b>🖨️ Print / Save as PDF</b> inside the invoice below to save a client-ready PDF.
                </span>
            </div>
            """, unsafe_allow_html=True)

            inv_no = f"INV-{datetime.now().strftime('%Y%m%d')}-01"
            issue_dt = datetime.now().strftime("%d %b %Y")
            due_dt = (datetime.now() + timedelta(days=3)).strftime("%d %b %Y")

            html_invoice = f"""
            <style>
                @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
                body {{ margin: 0; padding: 0; background: transparent; font-family: 'Inter', sans-serif; }}
                .inv-wrap {{
                    background: white;
                    color: #0f172a;
                    padding: 32px 36px;
                    border-radius: 16px;
                    font-family: 'Inter', sans-serif;
                    box-shadow: 0 4px 30px rgba(0,0,0,0.08);
                }}
                .inv-header {{
                    display: flex;
                    justify-content: space-between;
                    align-items: flex-start;
                    border-bottom: 3px solid #1e1b4b;
                    padding-bottom: 20px;
                    margin-bottom: 24px;
                }}
                .inv-title {{ margin: 0; font-size: 22px; font-weight: 800; color: #1e1b4b; letter-spacing: -0.5px; }}
                .inv-subtitle {{ margin: 4px 0 0 0; font-size: 12px; color: #64748b; }}
                .print-btn {{
                    background: linear-gradient(135deg, #4f46e5, #7c3aed);
                    color: white;
                    border: none;
                    padding: 10px 20px;
                    border-radius: 8px;
                    font-weight: 700;
                    cursor: pointer;
                    font-size: 13px;
                    letter-spacing: 0.2px;
                    box-shadow: 0 4px 12px rgba(79,70,229,0.35);
                    transition: all 0.2s ease;
                }}
                .print-btn:hover {{ transform: translateY(-1px); box-shadow: 0 6px 18px rgba(79,70,229,0.45); }}
                .party-grid {{
                    display: grid;
                    grid-template-columns: 1fr 1fr 1fr;
                    gap: 20px;
                    margin-bottom: 24px;
                    font-size: 14px;
                }}
                .party-label {{ font-size: 10px; font-weight: 700; color: #94a3b8; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 4px; }}
                .party-name {{ font-size: 16px; font-weight: 700; color: #0f172a; }}
                .party-meta {{ font-size: 13px; color: #475569; margin-top: 2px; }}
                .inv-table {{ width: 100%; border-collapse: collapse; margin-bottom: 24px; font-size: 14px; }}
                .inv-table thead tr {{ background: #f8fafc; }}
                .inv-table th {{ padding: 10px 14px; text-align: left; font-size: 11px; text-transform: uppercase; letter-spacing: 0.5px; color: #64748b; font-weight: 700; border-bottom: 2px solid #e2e8f0; }}
                .inv-table td {{ padding: 14px; border-bottom: 1px solid #f1f5f9; vertical-align: top; }}
                .milestone-num {{ display: inline-block; width: 22px; height: 22px; background: linear-gradient(135deg,#4f46e5,#7c3aed); color: white; border-radius: 50%; text-align: center; line-height: 22px; font-size: 11px; font-weight: 700; margin-right: 8px; }}
                .milestone-title {{ font-weight: 700; color: #0f172a; }}
                .milestone-sub {{ font-size: 12px; color: #64748b; margin-top: 3px; }}
                .amount-col {{ text-align: right; font-weight: 700; font-size: 15px; }}
                .totals-box {{ margin-left: auto; width: 260px; font-size: 14px; }}
                .total-row {{ display: flex; justify-content: space-between; padding: 5px 0; color: #475569; }}
                .total-row.grand {{ border-top: 2px solid #0f172a; margin-top: 6px; padding-top: 10px; font-weight: 800; font-size: 16px; color: #0f172a; }}
                .grand-val {{ color: #4f46e5; }}
                .footer-note {{
                    margin-top: 20px;
                    padding: 14px 16px;
                    background: linear-gradient(135deg, #f0f4ff, #f8f5ff);
                    border-left: 4px solid #4f46e5;
                    border-radius: 0 8px 8px 0;
                    font-size: 12px;
                    color: #334155;
                    line-height: 1.6;
                }}
                @media print {{
                    .print-btn {{ display: none !important; }}
                    .inv-wrap {{ box-shadow: none !important; border-radius: 0 !important; }}
                }}
            </style>
            <div class="inv-wrap">
                <div class="inv-header">
                    <div>
                        <h2 class="inv-title">PROFORMA INVOICE &amp; WORK ORDER</h2>
                        <p class="inv-subtitle">Protected by FreelanceShield OS &nbsp;·&nbsp; Invoice #{inv_no}</p>
                    </div>
                    <button class="print-btn" onclick="window.print()">🖨️ Print / Save as PDF</button>
                </div>

                <div class="party-grid">
                    <div>
                        <div class="party-label">From (Freelancer)</div>
                        <div class="party-name">{freelancer_name or 'Independent Freelancer'}</div>
                        <div class="party-meta">Service Provider</div>
                    </div>
                    <div>
                        <div class="party-label">Bill To (Client)</div>
                        <div class="party-name">{client_name or 'Valued Client'}</div>
                        <div class="party-meta">Project Buyer</div>
                    </div>
                    <div style="text-align:right;">
                        <div class="party-label">Invoice Dates</div>
                        <div class="party-meta"><b>Issue:</b> {issue_dt}</div>
                        <div class="party-meta"><b>Advance Due:</b> {due_dt}</div>
                    </div>
                </div>

                <table class="inv-table">
                    <thead>
                        <tr>
                            <th>Description / Milestone</th>
                            <th>Terms</th>
                            <th style="text-align:right;">Amount</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>
                                <span class="milestone-num">1</span>
                                <span class="milestone-title">Project Kickoff &amp; Upfront Deposit ({upfront_pct}%)</span>
                                <div class="milestone-sub">{free_revisions} revision rounds included &nbsp;·&nbsp; Extra revisions @ {sym}{extra_rev_cost}/round</div>
                            </td>
                            <td style="color:#64748b;">Due Before Start</td>
                            <td class="amount-col" style="color:#4f46e5;">{sym}{upfront_amt:,}</td>
                        </tr>
                        <tr>
                            <td>
                                <span class="milestone-num">2</span>
                                <span class="milestone-title">Final Handover &amp; IP Release ({100-upfront_pct}%)</span>
                                <div class="milestone-sub">Source files, deliverables, and all rights transferred upon receipt</div>
                            </td>
                            <td style="color:#64748b;">Due On Completion</td>
                            <td class="amount-col" style="color:#4f46e5;">{sym}{balance_amt:,}</td>
                        </tr>
                    </tbody>
                </table>

                <div class="totals-box">
                    <div class="total-row"><span>Subtotal</span><span>{sym}{total_fee:,}</span></div>
                    <div class="total-row"><span>GST / Tax ({tax_pct}%)</span><span>{sym}{tax_amt:,}</span></div>
                    <div class="total-row grand"><span>Grand Total</span><span class="grand-val">{sym}{grand_total:,}</span></div>
                </div>

                <div class="footer-note">
                    🔒 <b>Protection Terms:</b> Work commences upon receipt of the <b>{sym}{upfront_amt:,}</b> upfront deposit.
                    All source files and intellectual property rights transfer automatically upon final settlement.
                    {'&nbsp; &nbsp; ⏱️ <b>Late Penalty:</b> 5% per week on overdue amounts.' if late_fee else ''}
                    {'&nbsp; &nbsp; 🚫 <b>Kill Fee:</b> Advance is non-refundable on client cancellation.' if kill_clause else ''}
                </div>
            </div>
            """
            components.html(html_invoice, height=550, scrolling=True)

        with tab3:
            st.markdown("""
            <div style="display: flex; align-items: center; gap: 10px; padding: 12px 16px;
                        background: rgba(16,185,129,0.08); border: 1px solid rgba(52,211,153,0.25);
                        border-radius: 10px; margin-bottom: 16px;">
                <span style="font-size: 1.2rem;">📲</span>
                <span style="font-size: 0.85rem; color: #6ee7b7;">
                    Copy-paste ready messages in <b>English, Hinglish &amp; Corporate Email</b> formats!
                </span>
            </div>
            """, unsafe_allow_html=True)
            st.markdown('<div class="tab-content-wrapper">', unsafe_allow_html=True)
            st.markdown(st.session_state.pitch_md)
            st.markdown('</div>', unsafe_allow_html=True)

        with tab4:
            st.markdown("""
            <div class="section-num" style="margin-bottom: 16px;">
                <span class="section-num-badge">🚨</span>
                Deal Vulnerability &amp; Red Flag Report
            </div>
            """, unsafe_allow_html=True)
            st.markdown('<div class="tab-content-wrapper">', unsafe_allow_html=True)
            st.markdown(st.session_state.risk_md)
            st.markdown('</div>', unsafe_allow_html=True)

            st.markdown("""
            <div style="height: 1px; background: linear-gradient(90deg, transparent, rgba(99,102,241,0.4), transparent); margin: 20px 0;"></div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div class="section-num" style="margin-bottom: 12px;">
                <span class="section-num-badge">🥊</span>
                Live Scope-Creep Pushback Simulator
            </div>
            <p style="font-size: 0.85rem; color: #4b5563; margin-bottom: 12px;">
                Client just asked for free extra work? Paste their message → get a polite but firm reply that protects your revenue.
            </p>
            """, unsafe_allow_html=True)

            creep_msg = st.text_input(
                "Client's Unfair Request:",
                value="Bhai ek chota sa kaam aur tha, 2 extra reels aur 1 banner free me adjust kar do na same budget me please!"
            )
            if st.button("🛡️  Generate Polite Pushback Reply", use_container_width=True):
                with st.spinner("Drafting firm boundary reply..."):
                    pushback_prompt = f"""
                    The client ({client_name}) just sent this scope-creep message: "{creep_msg}".
                    According to our signed agreement, only {free_revisions} revisions are included and extra work costs {sym}{extra_rev_cost} (or requires a separate add-on quote).
                    Write 2 short, super-polite, relationship-friendly replies (1 in professional English, 1 in respectful Hinglish) that warmly say YES to helping them, but firmly state the extra add-on charge before starting the extra work.
                    """
                    reply_out = run_open_ai(
                        provider, api_key, ollama_url, model_choice,
                        "You help freelancers politely charge for extra out-of-scope work without losing the client.",
                        pushback_prompt
                    )
                    st.success("✅ Copy & Send This Reply:")
                    st.markdown('<div class="tab-content-wrapper">', unsafe_allow_html=True)
                    st.markdown(reply_out)
                    st.markdown('</div>', unsafe_allow_html=True)

    else:
        # ── Empty State ──
        st.markdown("""
        <div style="background: rgba(10,13,26,0.6); border: 1px solid rgba(99,102,241,0.15);
                    border-radius: 16px; padding: 50px 40px; text-align: center;
                    backdrop-filter: blur(12px);">
            <div style="font-size: 4rem; margin-bottom: 16px; animation: float 3s ease infinite;
                        filter: drop-shadow(0 0 24px rgba(99,102,241,0.5));">🛡️</div>
            <div style="font-size: 1.3rem; font-weight: 700; color: #e2e8f0; margin-bottom: 8px;
                        font-family: 'Space Grotesk', sans-serif;">
                Your Workspace is Ready
            </div>
            <div style="color: #374151; font-size: 0.9rem; max-width: 340px; margin: 0 auto 28px; line-height: 1.6;">
                Load a scenario or enter your project details to generate a full legal protection suite.
            </div>
            <div style="display: flex; flex-direction: column; align-items: center; gap: 10px; max-width: 360px; margin: 0 auto;">
                <div style="display: flex; align-items: center; gap: 12px; background: rgba(99,102,241,0.08);
                            border: 1px solid rgba(99,102,241,0.2); border-radius: 10px; padding: 12px 16px; width: 100%;">
                    <div style="width: 26px; height: 26px; background: linear-gradient(135deg,#6366f1,#8b5cf6);
                                border-radius: 7px; display: flex; align-items: center; justify-content: center;
                                font-size: 0.75rem; font-weight: 800; color: white; flex-shrink: 0;">1</div>
                    <span style="font-size: 0.85rem; color: #64748b; text-align: left;">
                        Click a <b style="color:#a5b4fc;">Quick-Load</b> button or type your project notes
                    </span>
                </div>
                <div style="display: flex; align-items: center; gap: 12px; background: rgba(99,102,241,0.08);
                            border: 1px solid rgba(99,102,241,0.2); border-radius: 10px; padding: 12px 16px; width: 100%;">
                    <div style="width: 26px; height: 26px; background: linear-gradient(135deg,#8b5cf6,#a78bfa);
                                border-radius: 7px; display: flex; align-items: center; justify-content: center;
                                font-size: 0.75rem; font-weight: 800; color: white; flex-shrink: 0;">2</div>
                    <span style="font-size: 0.85rem; color: #64748b; text-align: left;">
                        Configure your <b style="color:#a5b4fc;">deal, fees &amp; legal guardrails</b> in the sidebar
                    </span>
                </div>
                <div style="display: flex; align-items: center; gap: 12px; background: rgba(99,102,241,0.08);
                            border: 1px solid rgba(99,102,241,0.2); border-radius: 10px; padding: 12px 16px; width: 100%;">
                    <div style="width: 26px; height: 26px; background: linear-gradient(135deg,#4f46e5,#6366f1);
                                border-radius: 7px; display: flex; align-items: center; justify-content: center;
                                font-size: 0.75rem; font-weight: 800; color: white; flex-shrink: 0;">3</div>
                    <span style="font-size: 0.85rem; color: #64748b; text-align: left;">
                        Hit <b style="color:#a5b4fc;">🚀 Generate</b> to unlock your 4-tab workspace &amp; invoice
                    </span>
                </div>
            </div>
        </div>
        <style>
        @keyframes float {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-8px); }
        }
        </style>
        """, unsafe_allow_html=True)