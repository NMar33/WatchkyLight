import streamlit as st
from utils.settings_manager import load_settings, save_settings, reset_settings, default_settings
from utils.ui_components import display_settings_tables, display_settings_editor
from utils.ui_components import display_solution_ideas


PARAMS_TRANSLATION = {
    "initial_playback_delay_ms": "Задержка старта (мс)",
    "rebuffer_count": "Количество ребуферингов",
    "average_bitrate_kbps": "Средний битрейт (Кбит/с)"
}


def render_page():
    
    """Рендеринг страницы настройки QoE."""
    st.title("🔧 Настройка параметров оценки удовлетворенности")
    display_solution_ideas()

    # Загрузка текущих настроек
    settings = load_settings()

    # Отображение текущих настроек
    st.subheader("📋 Текущие настройки")
    display_settings_tables(settings, PARAMS_TRANSLATION)

    # Вкладки для редактирования настроек
    tab1, tab2 = st.tabs(["По устройствам", "По продолжительности"])
    with tab1:
        display_settings_editor(settings, PARAMS_TRANSLATION, "device")
    with tab2:
        display_settings_editor(settings, PARAMS_TRANSLATION, "duration")

    # Кнопки управления
    st.write("## Управление настройками")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("💾 Сохранить настройки"):
            save_settings(settings)
            st.rerun()
            st.success("Настройки успешно сохранены!")
    with col2:
        if st.button("📂 Загрузить настройки"):
            settings = load_settings()
            st.rerun()
    with col3:
        if st.button("🔄 Сбросить настройки"):
            reset_settings()
            st.rerun()

    st.write("Настройки сохраняются в файл `settings.json` и могут использоваться в других приложениях.")
