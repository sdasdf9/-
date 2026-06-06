FILE="students.txt"
echo "=== Статистика оценок ==="
sum=$(awk '{sum += $2} END {print sum}' "$FILE")
echo "Сумма оценок: $sum"
avg=$(awk '{sum += $2} END {print sum / NR}' "$FILE")
echo "Средняя оценка: $avg"
max=$(awk 'NR==1 {max=$2} $2 > max {max=$2} END {print max}' "$FILE")
echo "Максимальная оценка: $max"
