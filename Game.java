package com.hd.wuzi;


import java.util.ArrayList;

public class Game {
    public static ArrayList list=new ArrayList();
    public static boolean isover(int x,int y){
        int i = x;
        int j = y;
        int count = 0;
        //判断横向向左是否五连
        for (j = y; j >= 0 ; j--) {
            if (list.contains(i+","+j)) {
                count++;
            }else {
                break;
            }
        }

        //判断横向向右是否五连
        for (j = y; j <= 14 ; j++) {
            if (list.contains(i+","+j)) {
                count++;
            }else {
                break;
            }
        }
        count--;
        if (count >= 5) {
            System.out.println( ChessBroad.iswhite?"白":"黑"+ "棋胜！游戏结束！！！");
            return false;
        }

        //判断纵向向上是否五连
        i = x;
        j = y;
        count = 0;
        for (i = x; i >= 0 ; i--) {
            if (list.contains(i+","+j)) {
                count++;
            }else {
                break;
            }
        }
        //判断纵向向下是否五连
        for (i = x; i <= 14 ; i++) {
            if (list.contains(i+","+j)) {
                count++;
            }else {
                break;
            }
        }
        count--;
        if (count >= 5) {
            System.out.println( ChessBroad.iswhite?"白":"黑"+ "棋胜！游戏结束！！！");
            return false;
        }

        //判断左上是否五连
        count = 0;
        for (i = x,j = y; i >= 0 && j >=0 ; i--,j--) {
            if (list.contains(i+","+j)) {
                count++;
            }else {
                break;
            }
        }
        //判断右下是否五连
        for (i = x,j = y; i < 15 && j < 15 ; i++,j++) {
            if (list.contains(i+","+j)) {
                count++;
            }else {
                break;
            }
        }
        count--;
        if (count >= 5) {
            System.out.println( ChessBroad.iswhite?"白":"黑"+ "棋胜！游戏结束！！！");
            return false;
        }

        //判断左下是否五连
        count = 0;
        for (i = x,j = y; i < 15 && j >=0 ; i++,j--) {
            if (list.contains(i+","+j)) {
                count++;
            }else {
                break;
            }
        }
        //判断右上是否五连
        for (i = x,j = y; i >= 0 && j < 15 ; i--,j++) {
            if (list.contains(i+","+j)) {
                count++;
            }else {
                break;
            }
        }
        count--;
        if (count >= 5) {
            System.out.println(ChessBroad.iswhite?"白":"黑"+ "棋胜！游戏结束！！！");
            return false;
        }

        return true;
    }
}
