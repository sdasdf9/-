echo -e "Файл\tA\tT\tG\tC"
for file in *.fasta; do
    [ -f "$file" ] || continue
    if [ ! -s "$file" ]; then
        continue
    fi
    counts=$(awk '!/^>/ {
        line = toupper($0);
        a += gsub(/A/, "", line);
        t += gsub(/T/, "", line);
        g += gsub(/G/, "", line);
        c += gsub(/C/, "", line)
    }
    END {
        print a, t, g, c
    }' "$file")
    echo -e "$file\t$counts"
done
