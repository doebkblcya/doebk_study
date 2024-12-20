import java.util.Scanner;

public class study {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);  // 创建一个 Scanner 对象，用于读取用户输入
        String s;
        try {
            while (true) {
                s = scan.nextLine();  // 读取用户输入的一行字符串
                s = s.replace("你", "我");  // 将字符串中的 "你" 替换为 "我"
                s = s.replace("吗", "");  // 将字符串中的 "吗" 删除
                s = s.replace("？", "！");  // 将字符串中的 "？" 替换为 "！"
                System.out.println(s);  // 输出处理后的字符串
            }
        } finally {
            scan.close();  // 在程序结束时关闭 Scanner，释放资源
        }
    }
}
