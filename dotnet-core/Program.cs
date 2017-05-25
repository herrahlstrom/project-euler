using System;
using System.Diagnostics;
using System.Linq;
using System.Reflection;
using System.Text.RegularExpressions;

namespace ProjectEuler
{
	public class Program
	{
		public static void Main(string[] args)
		{
			IProblem oProblem = (from t in typeof(Program).GetTypeInfo().Assembly.GetTypes()
								 let ti = t.GetTypeInfo()
								 where ti.IsClass && !ti.IsAbstract
								 where typeof(IProblem).IsAssignableFrom(t)
								 let id = Regex.Replace(ti.Name, "[^0-9]", "")
								 orderby id descending
								 select (IProblem)Activator.CreateInstance(t)).First();

			Stopwatch sw = Stopwatch.StartNew();
			var answer = oProblem.Run();
			sw.Stop();

			Console.WriteLine("Answer: " + answer);
			Console.WriteLine(sw.ElapsedMilliseconds + " ms");

			if (Debugger.IsAttached)
			{
				Console.ReadLine();
			}

		}
	}
}
