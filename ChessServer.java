package com.hd.wuzi;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.InetAddress;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.ArrayList;
import java.util.Scanner;

public class ChessServer {
    public ArrayList list=new ArrayList();
    public static final int  mdk=7790;
    public static boolean gameover=true;

    public static void main(String[] args) throws IOException  {
        Scanner scanner=new Scanner(System.in);
        ChessBroad chessBroad=new ChessBroad();
        ServerSocket server=new ServerSocket(mdk);
        Socket client= server.accept();
        System.out.println("连接成功");
        InetAddress address=client.getInetAddress();
        System.out.println(address.getHostAddress());

        InputStream in= client.getInputStream();
        OutputStream ou=client.getOutputStream();
        Scanner sc=new Scanner(System.in);
        while(gameover){
            while(true){
                if(ChessBroad.broad[0][0]==null){
                    ChessBroad.init();
                    ChessBroad.draw();
                }
                System.out.println("请输入坐标:x,y");
                String send=sc.next();
                while(true){
                    if(!Game.list.contains(send)){
                        Game.list.add(send);
                        break;
                    }else{
                        System.out.println("已存在旗子");
                        send=sc.next();
                    }
                }
                ou.write(send.getBytes());
                Game.list.add(send);
                ChessBroad.iswhite=false;
                String []ss=send.split(",");
                int x=new Integer(ss[0]);
                int y=new Integer(ss[1]);
                ChessBroad.broad[x][y]=ChessBroad.iswhite ? " ○ ":" ● ";
                System.out.println(chessBroad.iswhite);
                ChessBroad.draw();
                if(!Game.isover(x, y)){
                    break;
                }
                System.out.println("等待对方落子");
                byte []buf=new byte[1024];
                int len =in.read(buf);
                String receive=new String(buf,0,len);
                System.out.println("白棋坐标："+receive);
                ChessBroad.iswhite=true;
                Game.list.add(receive);
                ss=receive.split(",");
                x=new Integer(ss[0]);
                y=new Integer(ss[1]);
                ChessBroad.broad[x][y]=ChessBroad.iswhite ? " ○ ":" ● ";
                ChessBroad.draw();
                gameover=Game.isover(x, y);
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
}
