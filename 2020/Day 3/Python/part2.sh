x=(
    1 3 5 7 1
)
y=(
    1 1 1 1 2
)

product=1
for i in {0..4}; do
    product=$(( $product*$(python main.py input.txt -x ${x[i]} -y ${y[i]} --notrees) ))
done
echo $product