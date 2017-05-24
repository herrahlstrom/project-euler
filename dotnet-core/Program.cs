using System;

namespace ProjectEuler
{
	public class Program
	{
		public static void Main(string[] args)
		{
			var answer = new Problem41().Run();
			Console.WriteLine("Answer: " + answer);

			if (System.Diagnostics.Debugger.IsAttached)
			{
				Console.ReadLine();
			}

		}
	}
}
