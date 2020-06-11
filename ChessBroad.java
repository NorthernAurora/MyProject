package com.hd.wuzi;

public class ChessBroad {
    public static boolean iswhite = true;
    public static String[][] broad = new String[15][15];
    private static final int mlineNum = 15;
    public static void init() {
        for (int i = 0; i < mlineNum; i++) {
            for (int j = 0; j < mlineNum; j++) {
                if (i == 0 && j == 0) {
                    broad[i][j] = "┏ ";
                } else if (i == 0 && j > 0 && j < 14) {
                    broad[i][j] = " ┳ ";
                } else if (j < 14 && j > 0 && i == 14) {
                    broad[i][j] = " ┻ ";
                } else if (i == 0 && j == 14) {
                    broad[i][j] = " ┓";
                } else if (i > 0 && i < 14 && j == 0) {
                    broad[i][j] = "┣ ";
                } else if (i > 0 && i < 14 && j == 14) {
                    broad[i][j] = " ┫";
                } else if (j == 0 && i == 14) {
                    broad[i][j] = "┗ ";
                } else if (j == 14 && i == 14) {
                    broad[i][j] = " ┛";
                } else {
                    broad[i][j] = " ╋ ";
                }
            }
        }
    }
    public static void draw () {

        for (int i = 0; i < broad.length; i++) {
            for (int j = 0; j < broad.length; j++) {
                System.out.print(broad[i][j]);
            }
            System.out.println();
        }
    }

}
