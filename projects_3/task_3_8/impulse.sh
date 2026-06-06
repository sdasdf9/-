if [ $# -lt 2 ]; then
    echo "Ошибка: недостаточно аргументов. Использование: $0 <имя гена> <уровень экспрессии>"
    exit 1
fi
gene_name="$1"
expression_level="$2"
echo "Экспрессия гена $gene_name составляет $expression_level единиц"
