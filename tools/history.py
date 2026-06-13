import json
import os

HISTORY_FILE = "research_history.json"


def load_history():

    if not os.path.exists(HISTORY_FILE):
        return {}

    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    except:
        return {}


def save_history(topic, report):

    history = load_history()

    history[topic] = report

    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(
            history,
            f,
            indent=4,
            ensure_ascii=False
        )


def get_topics():

    history = load_history()

    return list(history.keys())


def get_report(topic):

    history = load_history()

    return history.get(topic, "")