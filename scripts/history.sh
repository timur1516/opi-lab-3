#!/bin/bash

# Файл для сохранения diff
DIFF_FILE="$1"

# Проверка того что текущий коммит первый
is_first_commit() {
    if git rev-parse --verify HEAD^ 1>/dev/null 2>&1; then
        return 1
    else
        return 0
    fi
}

# Пробуем скопмпилировать самый новый коммит
# и если получилось то просто выходим (diff очевидно не нужен)
if ninja compile 1>/dev/null 2>&1; then
    echo "Компиляция успешна в ревизии $(git rev-parse HEAD)"
    echo "Это самая последняя ревизия, diff не создаётся"
    echo "Скрипт успешно завершён"
    exit 0
fi

# Начинаем в цикле перебирать ревизии
while true; do
    # Раз уж мы тут оказались, то текущий коммит не компилируется
    echo "Компиляция не удалась в ревизии $(git rev-parse HEAD)"

    # Проверяем, что текущий коммит не первый
    # Если первый, то просто выходим
    if is_first_commit; then
        echo "Достигнута первая ревизия, компиляция невозможна"
        echo "Скрипт завершён: нет рабочей ревизии"
        exit 0
    fi

    # Сохраняем текущий коммит (для выполнения diff)
    LAST_COMMIT=$(git rev-parse HEAD)

    # Получаем новый текущий коммит
    git checkout HEAD^ >/dev/null 2>&1
    CURRENT_COMMIT=$(git rev-parse HEAD)

    echo "Переключение на ревизию $CURRENT_COMMIT"

    # Если удалось скомпилировать, то сохраняем diff
    if ninja compile 1>/dev/null 2>&1; then
        echo "Компиляция успешна в ревизии $CURRENT_COMMIT"
        git diff "$CURRENT_COMMIT" "$LAST_COMMIT" >"$DIFF_FILE"
        echo "Diff успешно сохранён в $DIFF_FILE"
        echo "Скрипт успешно завершён"
        exit 0
    fi
done
