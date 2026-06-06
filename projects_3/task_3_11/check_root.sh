check_root() {
    if [[ $EUID -ne 0 ]]; then
        echo "Предупреждение: Скрипт должен быть запущен от суперпользователя (root)." >&2
        exit 1
    fi
}
check_root
echo "Скрипт запущен от root."
