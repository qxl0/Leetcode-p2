class Solution {
    public String losingPlayer(int x, int y) {
        // 75->x, 10->y
        // A -> B -> A ...
        // 115, 75 + 4*10
        int turn = 0; // A
        while (true) {
            if (x>=1 && y>=4) {
                turn = 1-turn;
                x -= 1;
                y -= 4;
            }
            else {
                if (turn==1) {
                    return "Alice";
                }
                else {
                    return "Bob";
                }
            }
        }
    }
}