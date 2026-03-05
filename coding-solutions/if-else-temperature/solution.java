class Solution {
    public String solve(int temperature) {

        if (temperature > 30) {
            return "hot";
        } 
        else if (temperature >= 15) {
            return "warm";
        } 
        else if (temperature >= 0) {
            return "cold";
        } 
        else {
            return "freezing";
        }

    }
}