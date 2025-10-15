using System;

namespace C
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int num = Convert.ToInt32(Console.ReadLine());
            if (num >= 13)
            {
                num += 1;
            }
            Console.Write(num);
        }
    }
}