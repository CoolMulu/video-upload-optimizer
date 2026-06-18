import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("📊 Video Upload Optimizer")

uploaded_file = st.file_uploader("Upload CSV", type="csv")

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    # 清理空值
    df = df.dropna(subset=["Time Posted", "Day", "Views Day 3"])

    # 提取小时
    df["hour"] = df["Time Posted"].str.extract(r"(\d+):")[0]

    df["hour"] = pd.to_numeric(
        df["hour"],
        errors="coerce"
    ).fillna(0).astype(int)

    # 提取 AM / PM
    df["ampm"] = df["Time Posted"].str.extract(r"(AM|PM)")

    # 转换 24 小时制
    df["hour_24"] = df.apply(
        lambda x: x["hour"] if x["ampm"] == "AM" else x["hour"] + 12,
        axis=1
    )

    # 最佳星期
    best_day = (
        df.groupby("Day")["Views Day 3"]
        .mean()
        .sort_values(ascending=False)
    )

    st.subheader("🔥 Best Day")
    st.write(best_day)

    # 最佳时间
    best_time = (
        df.groupby("hour_24")["Views Day 3"]
        .mean()
        .sort_values(ascending=False)
    )

    st.subheader("🔥 Best Time")
    st.write(best_time)

    # 热力图
    pivot = df.pivot_table(
        index="Day",
        columns="hour_24",
        values="Views Day 3",
        aggfunc="mean"
    )

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.heatmap(
        pivot,
        cmap="YlOrRd",
        annot=True,
        fmt=".0f",
        ax=ax
    )

    st.subheader("📈 Upload Performance Heatmap")
    st.pyplot(fig)

    # 最佳组合
    best_combo = (
        df.groupby(["Day", "hour_24"])["Views Day 3"]
        .mean()
        .sort_values(ascending=False)
        .head(1)
    )

    day = best_combo.index[0][0]
    hour = best_combo.index[0][1]

    st.success(f"🚀 Best Upload Time: {day} {hour}:00")