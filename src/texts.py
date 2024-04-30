from typing import List

from src.db import Task

main_text = '''Привет!

1. Используй команду /add для добавления задачи
2. Используй команду /tsk для просмотра всех задач'''


def create_text_tasks(tasks: List[Task]) -> str:
    text = '📋Список задач:\n\n'
    for task in tasks:
        date = task.create_date.strftime('%Y-%m-%d %H:%M')
        text += f'#{task.id}, {task.title}: {task.description}\n{date}\n\n'
    return text