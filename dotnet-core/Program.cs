using System;
using System.Diagnostics;

namespace ProjectEuler
{
	public class Program
	{
		public static void Main(string[] args)
		{
			Stopwatch sw = Stopwatch.StartNew();
			var answer = new Problem41().Run();
			Console.WriteLine("Answer: " + answer);

			sw.Stop();
			Console.WriteLine(sw.ElapsedMilliseconds + " ms");

			if (System.Diagnostics.Debugger.IsAttached)
			{
				Console.ReadLine();
			}

		}
	}
}
