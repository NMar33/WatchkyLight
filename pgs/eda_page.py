import streamlit as st
from utils.data_loader import load_data
from utils.formulas import calculate_user_experience
from utils.ui_components import (
    display_summary_statistics,
    apply_filters,
    render_region_analysis,
    render_qoe_metrics,
    render_playback_delay_histogram,
    render_time_series_analysis,
    render_comparison_chart
)
import pandas as pd
from utils.ui_components import display_solution_ideas

from utils.settings_manager import load_settings
rules = load_settings()

def render_page():
    """Основная функция для рендеринга страницы EDA."""
    st.title("📊 Анализ данных ClickHouse")
    display_solution_ideas()

    # Загрузка данных
    df = load_data()

    # Отображение общей статистики
    display_summary_statistics(df)

    # Применение фильтров
    filtered_df = apply_filters(df)

    memory_coefficient = st.sidebar.slider("Коэффициент злопамятности", 1, 5, 3)
    filtered_df = calculate_user_experience(filtered_df, rules['device'], rules['duration'], memory_coefficient)

    st.sidebar.success("Пользовательский опыт рассчитан и добавлен к данным.")

    # Анализ регионов
    render_region_analysis(filtered_df)

    # Отображение метрик QoE
    render_qoe_metrics(filtered_df)

    # Гистограмма задержки воспроизведения
    render_playback_delay_histogram(filtered_df)

    # Анализ пользовательского опыта во времени
    st.header("📈 Анализ пользовательского опыта во времени")
    time_group = st.radio("Выберите уровень агрегации:", ['День', 'Час'], index=0)

    if time_group == 'День':
        filtered_df['time_group'] = pd.to_datetime(filtered_df['timestamp']).dt.date
    else:
        filtered_df['time_group'] = pd.to_datetime(filtered_df['timestamp']).dt.floor('H')

    render_time_series_analysis(filtered_df, time_group)

    # Сравнение метрик
    time_metrics = filtered_df.groupby('time_group').agg({
        'initial_playback_delay_ms': 'mean',
        'rebuffer_count': 'mean',
        'average_bitrate_kbps': 'mean',
        'user_experience': 'mean'
    }).reset_index()

    metrics_to_compare = st.multiselect(
        "Выберите метрики для сравнения:",
        ['initial_playback_delay_ms', 'rebuffer_count', 'average_bitrate_kbps', 'user_experience'],
        default=['user_experience']
    )
    render_comparison_chart(time_metrics, metrics_to_compare)