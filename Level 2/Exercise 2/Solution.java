import java.util.Arrays;

public class Solution {

    private static int[] count;

    public static int solution(int[] l) {
        int res = 0;
        count = new int[10];
        for (int i = 0; i < l.length; i++) {
            count[l[i]]++;
        }
        System.out.println(Arrays.toString(count));
        res = maxValue(0, l.length);
        count = null;
        return res;
    }

    public static int maxValue(int curr, int maxLen) {
        if (maxLen == 0)
            return (curr % 3 == 0) ? curr : 0;

        int max = maxValue(curr, maxLen - 1);
        for (int i = 9; i >= 0; i--) {
            if (count[i] <= 0)
                continue;
            count[i]--;
            max = Math.max(max, maxValue(curr * 10 + i, maxLen - 1));
            count[i]++;
        }
        return max;
    }
}