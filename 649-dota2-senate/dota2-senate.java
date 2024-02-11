class Solution {
    int n;
    public String predictPartyVictory(String senate) {
        n = senate.length();
        boolean[] banned = new boolean[n];

        int rcount = 0, dcount = 0;
        for (var ch: senate.toCharArray()) {
            if (ch=='R')
                rcount+=1;
            else
                dcount+=1;
        }

        int turn = 0;

        while (rcount>0 && dcount>0) {
            if (banned[turn]) 
            {
                turn = (turn+1)%n;
                continue;
            }
                
            if (senate.charAt(turn)=='R') {
                ban(senate, banned, 'D', (turn+1)%n);
                dcount -= 1;
            }
            else {
                ban(senate, banned, 'R', (turn+1)%n);
                rcount -= 1;
            }

            turn = (turn+1)%n;
        }

        return dcount == 0? "Radiant" : "Dire";
    }

    private void ban(String senate, boolean[] banned, Character p, int startfrom) {
        // ban from startfrom p
        int i = startfrom;

        while (true) {
            if (senate.charAt(i)==p && !banned[i]) {
                banned[i] = true;
                break;
            }
            i = (i+1)%n;
        }
    }
}