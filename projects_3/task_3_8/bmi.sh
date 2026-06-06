read -p 'Введите вес (кг): ' weight
read -p 'Введите рост (м): ' height
BMI=$(echo "scale=2; $weight / ($height * $height)" | bc)
echo "Индекс массы тела: $BMI"
