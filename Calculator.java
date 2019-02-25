import javax.swing.*;
import java.awt.event.*;
import java.awt.*;
class Calculator extends JFrame{
JTextField d1;
JTextField d2;
JButton add;
JButton sub;
JButton mul;
JButton div;
JButton del;
JButton perc;
JButton clear;
JButton sign;
JButton dot;
JButton equal;
JButton one;
JButton two;
JButton three;
JButton four;
JButton five;
JButton six;
JButton seven;
JButton eight;
JButton nine;
JButton zero;
JButton dummy;
double ans;
int op;
Calculator(){
ans=0;
setTitle("Calculator");
d1=new JTextField();
d2=new JTextField();
Font f1=new Font("Arial Black",Font.BOLD,23);
d2.setFont(f1);
add=new JButton("+");
sub=new JButton("-");
mul=new JButton("*");
div=new JButton("/");
del=new JButton("<--");
dot=new JButton(".");
perc=new JButton("SQRT");
clear=new JButton("C");
sign=new JButton("+/-");
equal=new JButton("=");
one=new JButton("1");
two=new JButton("2");
three=new JButton("3");
four=new JButton("4");
five=new JButton("5");
six=new JButton("6");
seven=new JButton("7");
eight=new JButton("8");
nine=new JButton("9");
zero=new JButton("0");
dummy=new JButton();

d1.setHorizontalAlignment(JTextField.RIGHT);
d2.setHorizontalAlignment(JTextField.RIGHT);

d1.setBounds(50,25,350,20); d1.setEditable(false);
d2.setBounds(50,55,350,45);
clear.setBounds(50,130,80,30);	del.setBounds(140,130,80,30);	perc.setBounds(230,130,80,30);	div.setBounds(320,130,80,30);
seven.setBounds(50,170,80,30);	eight.setBounds(140,170,80,30);	nine.setBounds(230,170,80,30);	mul.setBounds(320,170,80,30);
four.setBounds(50,210,80,30);	five.setBounds(140,210,80,30);	six.setBounds(230,210,80,30);	sub.setBounds(320,210,80,30);
one.setBounds(50,250,80,30);	two.setBounds(140,250,80,30);	three.setBounds(230,250,80,30);	add.setBounds(320,250,80,30);
sign.setBounds(50,290,80,30);	zero.setBounds(140,290,80,30);	dot.setBounds(230,290,80,30);	equal.setBounds(320,290,80,30);

one.addActionListener(new ActionListener(){
	public void actionPerformed(ActionEvent e){
		d2.setText(d2.getText()+"1");
	}
});
two.addActionListener(new ActionListener(){
	public void actionPerformed(ActionEvent e){
		d2.setText(d2.getText()+"2");
	}
});
three.addActionListener(new ActionListener(){
	public void actionPerformed(ActionEvent e){
		d2.setText(d2.getText()+"3");
	}
});
four.addActionListener(new ActionListener(){
	public void actionPerformed(ActionEvent e){
		d2.setText(d2.getText()+"4");
	}
});
five.addActionListener(new ActionListener(){
	public void actionPerformed(ActionEvent e){
		d2.setText(d2.getText()+"5");
	}
});
six.addActionListener(new ActionListener(){
	public void actionPerformed(ActionEvent e){
		d2.setText(d2.getText()+"6");
	}
});
seven.addActionListener(new ActionListener(){
	public void actionPerformed(ActionEvent e){
		d2.setText(d2.getText()+"7");
	}
});
eight.addActionListener(new ActionListener(){
	public void actionPerformed(ActionEvent e){
		d2.setText(d2.getText()+"8");
	}
});
nine.addActionListener(new ActionListener(){
	public void actionPerformed(ActionEvent e){
		d2.setText(d2.getText()+"9");
	}
});
zero.addActionListener(new ActionListener(){
	public void actionPerformed(ActionEvent e){
		d2.setText(d2.getText()+"0");
	}
});
del.addActionListener(new ActionListener(){
	public void actionPerformed(ActionEvent e){
		try{String s=d2.getText();
		d2.setText(s.substring(0,s.length()-1));}
		catch(Exception ex){}
	}
});

add.addActionListener(new ActionListener(){
	public void actionPerformed(ActionEvent e){
		String s=d2.getText();
		try{double v=Double.parseDouble(s); done(v);op=1;
		if(ans%1==0.00) d1.setText(String.valueOf((int)ans)+"+");
		else d1.setText(String.valueOf(ans)+"+");
		d2.setText("");}
		catch(Exception ex){d2.setText("MATH SYNTAX ERROR");ans=0;op=0;}
		
	}
});
sub.addActionListener(new ActionListener(){
	public void actionPerformed(ActionEvent e){
		String s=d2.getText();
		try{double v=Double.parseDouble(s); done(v);op=2;
		if(ans%1==0.00) d1.setText(String.valueOf((int)ans)+"-");
		else d1.setText(String.valueOf(ans)+"-");
		d2.setText("");}
		catch(Exception ex){d2.setText("MATH SYNTAX ERROR");ans=0;op=0;}
		
	}
});
mul.addActionListener(new ActionListener(){
	public void actionPerformed(ActionEvent e){
		String s=d2.getText();
		try{double v=Double.parseDouble(s); done(v);op=3;
		if(ans%1==0.00) d1.setText(String.valueOf((int)ans)+"*");
		else d1.setText(String.valueOf(ans)+"*");
		d2.setText("");}
		catch(Exception ex){d2.setText("MATH SYNTAX ERROR");ans=0;op=0;}
		
	}
});
div.addActionListener(new ActionListener(){
	public void actionPerformed(ActionEvent e){
		String s=d2.getText();
		try{double v=Double.parseDouble(s); done(v);op=4;
		if(ans%1==0.00) d1.setText(String.valueOf((int)ans)+"/");
		else d1.setText(String.valueOf(ans)+"/");
		d2.setText("");}
		catch(Exception ex){d2.setText("MATH SYNTAX ERROR");ans=0;op=0;}
		
	}
});
perc.addActionListener(new ActionListener(){
	public void actionPerformed(ActionEvent e){
		String s=d2.getText();
		try{double v=Double.parseDouble(s);ans=v; op=5; done(v);op=5;
		if(ans%1==0.00) d1.setText(String.valueOf((int)ans));
		else d1.setText(String.valueOf(ans));
		d2.setText(String.valueOf(ans));}
		catch(Exception ex){d2.setText("MATH SYNTAX ERROR");ans=0;op=0;}
		
	}
});
clear.addActionListener(new ActionListener(){
	public void actionPerformed(ActionEvent e){
		op=0;ans=0;d1.setText("");d2.setText("");
	}
});
equal.addActionListener(new ActionListener(){
	public void actionPerformed(ActionEvent e){
		String s=d2.getText();
		try{double v=Double.parseDouble(s); done(v);op=0;
		if(ans%1==0.00) d1.setText(String.valueOf((int)ans));
		else d1.setText(String.valueOf(ans));
		d2.setText(d1.getText());}
		catch(Exception ex){d2.setText("MATH SYNTAX ERROR");ans=0;op=0;}
		
	}
});
sign.addActionListener(new ActionListener(){
	public void actionPerformed(ActionEvent e){
		String s=d2.getText();
		char c='-';
		try{double v=Double.parseDouble(s);
		if(s.charAt(0)=='-') d2.setText(s.substring(1,s.length()));
		else d2.setText("-"+s);
		}catch(Exception ex){d2.setText("MATH SYNTAX ERROR");ans=0;op=0;}
		
	}
});
dot.addActionListener(new ActionListener(){
	public void actionPerformed(ActionEvent e){
		String s=d2.getText();
		try{double v=Double.parseDouble(s);
		d2.setText(s+".");
		}catch(Exception ex){d2.setText("MATH SYNTAX ERROR");ans=0;op=0;}
		
	}
});
add(d1);
add(d2);
add(add);
add(sub);
add(mul);
add(div);
add(del);
add(dot);
add(equal);
add(perc);
add(clear);
add(sign);
add(one);
add(two);
add(three);
add(four);
add(five);
add(six);
add(seven);
add(eight);
add(nine);
add(zero);
add(dummy);
setVisible(true);
setSize(450,450);
setLayout(null);
}
void done(double v){
	if(op==1) ans=ans+v;
	else if(op==2) ans=ans-v;
	else if(op==3) ans=ans*v;
	else if(op==4) ans=ans/v;
	else if(op==5) ans=Math.sqrt(ans);
	else ans=v;
}
}
class Run{
	public static void main(String args[]){
		new Calculator();
	}
}