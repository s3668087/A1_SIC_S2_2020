import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class keypad extends JFrame {
    private int digit_count = 15;
    private String code_one,code_two,code_three,mastercode;
    public static void main(String[] args) {
        System.out.println("WARNING: Make sure the CMOS battery is at a good level. Power loss will permantly prevent access.");

        keypad start_keypad = new keypad();
    }

    private keypad() {


        setTitle("Keypad");
        setSize(300, 400);
        setLayout(new GridLayout(5, 3));     

        JLabel lab_person  = new JLabel("Person 1:");   add(lab_person); 
        JLabel lab_digits   = new JLabel(" ");   add(lab_digits); 
        JLabel lab_status  = new JLabel("Initialisation");   add(lab_status); 

        JButton btn_1 = new JButton("1");   add(btn_1); btn_1.addActionListener(new ActionListener() { public void actionPerformed(ActionEvent e) { handleKeypad(btn_1.getText()); } });
        JButton btn_2 = new JButton("2");   add(btn_2); btn_2.addActionListener(new ActionListener() { public void actionPerformed(ActionEvent e) { handleKeypad(btn_2.getText()); } });
        JButton btn_3 = new JButton("3");   add(btn_3); btn_3.addActionListener(new ActionListener() { public void actionPerformed(ActionEvent e) { handleKeypad(btn_3.getText()); } });
        JButton btn_4 = new JButton("4");   add(btn_4); btn_4.addActionListener(new ActionListener() { public void actionPerformed(ActionEvent e) { handleKeypad(btn_4.getText()); } });
        JButton btn_5 = new JButton("5");   add(btn_5); btn_5.addActionListener(new ActionListener() { public void actionPerformed(ActionEvent e) { handleKeypad(btn_5.getText()); } });
        JButton btn_6 = new JButton("6");   add(btn_6); btn_6.addActionListener(new ActionListener() { public void actionPerformed(ActionEvent e) { handleKeypad(btn_6.getText()); } });
        JButton btn_7 = new JButton("7");   add(btn_7); btn_7.addActionListener(new ActionListener() { public void actionPerformed(ActionEvent e) { handleKeypad(btn_7.getText()); } });
        JButton btn_8 = new JButton("8");   add(btn_8); btn_8.addActionListener(new ActionListener() { public void actionPerformed(ActionEvent e) { handleKeypad(btn_8.getText()); } });
        JButton btn_9 = new JButton("9");   add(btn_9); btn_9.addActionListener(new ActionListener() { public void actionPerformed(ActionEvent e) { handleKeypad(btn_9.getText()); } });
        JButton btn_0 = new JButton("0");   add(btn_0); btn_0.addActionListener(new ActionListener() { public void actionPerformed(ActionEvent e) { handleKeypad(btn_0.getText()); } });
        JLabel lab_blank_3  = new JLabel("");   add(lab_blank_3); 

        setVisible(true);
    }

    private String handleKeypad(String x ) {      
        if ( mastercode == null && digit_count <= 0 ){      
            System.out.println("Mastercode is now set");
            System.out.println(digit_count + " " + code_one + " " + code_two + " " + code_three);

        } 
        else { 

        }

        if ( digit_count > 10 ){
            if ( code_one == null ) code_one = x;
            else code_one = code_one+x; 
            
        }
        else if ( digit_count > 5 ){ 
            if ( code_two == null ) code_two = x;
            else code_two = code_two+x; 
            
        }
        else if ( digit_count > 0 ){ 
            if ( code_three == null ) code_three = x;
            else code_three = code_three+x; 
            
        }

        digit_count--;
        //System.out.println(x + " " + digit_count + " " + code_one + " " + code_two + " " + code_three);
        return "OK";
    }
}