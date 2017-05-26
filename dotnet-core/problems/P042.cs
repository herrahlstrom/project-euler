using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Net;
using System.Text;

namespace ProjectEuler
{
    class P042 : IProblem
    {
        private const string WordsUrl = "https://projecteuler.net/project/resources/p042_words.txt";
        private string WordsLocalPath = Path.Combine(Path.GetTempPath(), "projecteuler-042-words.txt");
        public long Run()
        {
            List<long> triangleNumbers = GetTriangleNumbers().Take(1000).ToList();

            return (from word in GetWords()
                    let wordSum = word.Sum(c => c - 64)
                    where triangleNumbers.Contains(wordSum)
                    select word).Count();
        }
        private IEnumerable<string> GetWords()
        {
            if (File.Exists(WordsLocalPath))
            {
                Console.WriteLine("Existing file " + WordsLocalPath);
            }
            else
            {
                using (var wc = new WebClient())
                {
                    Console.WriteLine("Download " + WordsUrl);
                    Console.WriteLine("	-> " + WordsLocalPath);
                    wc.DownloadFile(WordsUrl, WordsLocalPath);
                }
            }
            string data = File.ReadAllText(WordsLocalPath);
            string[] wordsArr = data.Split(',');
            return from word in wordsArr
                   select word.Trim('\"');
        }
        private IEnumerable<long> GetTriangleNumbers()
        {
            long n = 1;
            while (true)
            {
                yield return (long)(0.5 * n * (n + 1));
                n += 1;
            }
        }
    }
}
