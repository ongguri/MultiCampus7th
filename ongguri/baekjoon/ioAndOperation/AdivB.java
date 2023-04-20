package baekjoon.ioAndOperation;

import java.io.*;
import java.util.StringTokenizer;

public class AdivB {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        double div = Integer.parseInt(st.nextToken());

        while(st.countTokens() != 0) {
            div /= Integer.parseInt(st.nextToken());
        }

        System.out.println(div);
    }
}
