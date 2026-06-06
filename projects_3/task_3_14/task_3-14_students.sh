FILE="students.txt"
echo "=== Имена студентов ==="
awk '{print $1}' "$FILE"
echo
echo "=== Оценки студентов ==="
awk '{print $2}' "$FILE"
echo
echo "=== Номер строки и имя ==="
awk '{print NR, $1}' "$FILE"
