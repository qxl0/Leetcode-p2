class Solution {
    public int[] deckRevealedIncreasing(int[] deck) {
        Deque<Integer> dq = new ArrayDeque<>();
        for (int i=0;i<deck.length;i++) {
            dq.add(i);
        }

        Arrays.sort(deck);
        int[] ret = new int[deck.length];
        for (var i=0;i<deck.length;i++) {
            ret[dq.pollFirst()] = deck[i];
            if (!dq.isEmpty()) {
                dq.add(dq.removeFirst());
            }
        }
        return ret;

    }
}