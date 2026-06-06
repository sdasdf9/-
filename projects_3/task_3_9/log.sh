file="./system.log"
error=1
if [ -f "$file" ]; then
    echo "Лог-файл найден."
else
    echo "Ошибка: файл не существует."
fi

# 2. Числовое сравнение через Case
case $error in
    0)
        echo "Статус: Ошибок нет." ;;
    1)
        echo "Статус: Критическая ошибка!" ;;
    *)
        echo "Статус: Неизвестный код." ;;
esac
