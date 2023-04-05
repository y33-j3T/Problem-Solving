public class IntegerTriple implements Comparable<IntegerTriple> {
    protected Integer first; // source vertex
    protected Integer second; // adjacent vertex
    protected Integer third; // weight

    public IntegerTriple(Integer first, Integer second, Integer third) {
        this.first = first;
        this.second = second;
        this.third = third;
    }

    // sort by weight
    public int compareTo(IntegerTriple o) {
        return this.third() - o.third();
    }

    public Integer first() { return first; }
    public Integer second() { return second; }
    public Integer third() { return third; }
}
