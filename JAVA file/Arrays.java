import java.util.Scanner;
public class Arrays
{
    public static void main(String[] args)
    {
        int [] number1={2,4,6,8,10};
        int [] number2={2,4,6,8,10};
        int temp=0;
        int i=0;

        if (number1.length!=number2.length)
        {
            System.out.println("Arrays not equal");
        }
        else
        {
            while (i<number1.length)
            {
                if (number1[i]==number2[i])
                {
                    temp=temp+1;
                }
                i=i+1;
            }
            if (temp==number1.length)
            {
                System.out.println("The arrays are equal.");
            }
            else
            {
                System.out.println("The arrays are not equal.");
            }
        }
        System.out.println("\n");

        /*
        int [] number3=new int[3];
        int [] number4=new int[3];
        for (int j=0;j<number3.length;j++)
        {
            System.out.println("Write the element to be inserted in the array NUMBERS3:");
            Scanner kb=new Scanner(System.in);
            number3[j]=kb.nextInt();
        }
        System.out.println("\n");
        int m=number3.length-1;
        for (int j=0;j<number4.length;j++)
        {
            number4[j]=number3[m];
            m=m-1;
        }
        for (int val:number4)
        {
            System.out.println(val);
        }

         */

        int [] number={7,8,10,6,5};
        int tempo=0;
        for (int k=0;k<number.length;k++)
        {
            for (int n=0;n<number.length;n++)
            {
                if (number[k]>number[n])
                {
                    tempo=tempo+1;
                }
            }
            if (tempo==number.length-1)
            {
                System.out.println(number[k]);
            }
            else
            {
                tempo=0;
            }

        }







    }
}
