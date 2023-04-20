package baekjoon.ioAndOperation;

import java.io.*;
import java.util.StringTokenizer;

public class AplusB {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int sum = 0;

        while(st.countTokens() != 0) {
            sum += Integer.parseInt(st.nextToken());
        }

        System.out.println(sum);
    }
}
