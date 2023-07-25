using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AppArbolBinario
{
    internal class CArbolBinario
    {
        // Atributos
        CNodo raiz;

        // Constructor
        public CArbolBinario()
        {
            raiz = null;
        }

        // Metodos
        public void Insertar(int info)
        {
            CNodo nuevo;
            nuevo = new CNodo(info);
            if (raiz == null)
                raiz = nuevo;
            else
            {
                CNodo anterior = null, reco;
                reco = raiz;
                while (reco != null)
                {
                    anterior = reco;
                    if (info < reco.info)
                        reco = reco.izq;
                    else
                        reco = reco.der;
                }

                if (info < anterior.info)
                    anterior.izq = nuevo;
                else
                    anterior.der = nuevo;
            }
        }

        private void ImprimirPre(CNodo reco)
        {
            if (reco != null)
            {
                Console.Write(reco.info + " ");
                ImprimirPre(reco.izq);
                ImprimirPre(reco.der);
            }
        }

        private void ImprimirIn(CNodo reco)
        {
            if (reco != null)
            {
                ImprimirIn(reco.izq);
                Console.Write(reco.info + " ");
                ImprimirIn(reco.der);
            }
        }

        private void ImprimirPost(CNodo reco)
        {
            if (reco != null)
            {
                ImprimirPost(reco.izq);
                ImprimirPost(reco.der);
                Console.Write(reco.info + " ");
            }
        }

        public void ImprimirPre()
        {
            ImprimirPre(raiz);
            Console.WriteLine();
        }

        public void ImprimirIn()
        {
            ImprimirIn(raiz);
            Console.WriteLine();
        }

        public void ImprimirPost()
        {
            ImprimirPost(raiz);
            Console.WriteLine();
        }
    }
}
