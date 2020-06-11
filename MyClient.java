package com.hd.wuzi;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.Socket;
import java.util.Scanner;
import java.util.zip.CheckedInputStream;

public class MyClient {
    public static final String mip="127.0.0.1";
    public static boolean gameover=true;
    public static void main(String[] args) throws IOException {
        ChessBroad chessBroad=new ChessBroad();
        Socket socket=new Socket(mip,ChessServer.mdk);
        OutputStream ou=socket.getOutputStream();
        InputStream in =socket.getInputStream();
        Scanner scanner=new Scanner(System.in);
        while(gameover){
            while(true){
                if(ChessBroad.broad[0][0]==null){
                    ChessBroad.init();
                    ChessBroad.draw();
                }
                System.out.println("等待对方落子");
                byte[] buf=new byte[1024];
                int len=in.read(buf);
                String creceive=new String(buf,0,len);
                System.out.println("获得黑棋坐标："+creceive);
                ChessBroad.iswhite=false;
                Game.list.add(creceive);
                String []ss=creceive.split(",");
                int x=new Integer(ss[0]);
                int y=new Integer(ss[1]);
                ChessBroad.broad[x][y]=ChessBroad.iswhite ? " ○ ":" ● ";
                ChessBroad.draw();
                if(!Game.isover(x, y)){
                    break;
                }
                System.out.println("请输入坐标:x,y");
                String line= scanner.next();
                while(true){
                    if(!Game.list.contains(line)){
                        Game.list.add(line);
                        break;
                    }else{
                        System.out.println("已存在旗子");
                        line=scanner.next();
                    }
                }
                ou.write(line.getBytes());
                Game.list.add(line);
                ChessBroad.iswhite=true;
                ss=line.split(",");
                x=new Integer(ss[0]);
                y=new Integer(ss[1]);
                ChessBroad.broad[x][y]=ChessBroad.iswhite ? " ○ ":" ● ";
                ChessBroad.draw();
                gameover=Game.isover(x, y);
            }
            System.out.println("请选择：1：重新开始，2：退出");
            int op=scanner.nextInt();
            if (op==1){
                gameover=true;
            }else if(op==2){
                System.exit(0);
            }
        }
    }
}