using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Listas
{
    public class CNodoLista
    {
        //#region Atributos
        private Object? aElemento;
        private CNodoLista? aSgte;
        //#endregion Propiedades
        //#region Constructores
        public CNodoLista()
        {
            aElemento = null;
            aSgte = null;
        }
        public CNodoLista(Object pElemento)
        {
            aElemento = pElemento;
            aSgte = null;
        }
        public CNodoLista(Object pElemento, CNodoLista pNodo)
        {
            aElemento = pElemento;
            aSgte = pNodo;
        }
        //#endregion Constructores
        //#region Propiedades
        public object Elemento
        {
            set { aElemento = value; }
            get { return aElemento; }
        }
        public CNodoLista Sgte
        {
            set { aSgte = value; }
            get { return aSgte; }
        }
        //#endregion Propiedades
    }

    //    public class CNodoListaCircular
    //{
    //    private Object aElemento;
    //    private CNodoListaCircular aSgte;
//
    //    public CNodoListaCircular()
    //    {
    //        aElemento = null;
    //        aSgte = null;
    //    }
//
    //    public CNodoListaCircular(Object pElemento)
    //    {
    //        aElemento = pElemento;
    //        aSgte = null;
    //    }
//
    //    public CNodoListaCircular(Object pElemento, CNodoListaCircular pNodo)
    //    {
    //        aElemento = pElemento;
    //        aSgte = pNodo;
    //    }
//
    //    public object Elemento
    //    {
    //        set { aElemento = value; }
    //        get { return aElemento; }
    //    }
//
    //    public CNodoListaCircular Sgte
    //    {
    //        set { aSgte = value; }
    //        get { return aSgte; }
    //    }
    //}
//
    //    public class CNodoListaDoble
    //{
    //    private Object aElemento;
    //    private CNodoListaDoble aSgte;
    //    private CNodoListaDoble aAnt;
//
    //    public CNodoListaDoble()
    //    {
    //        aElemento = null;
    //        aSgte = null;
    //        aAnt = null;
    //    }
//
    //    public CNodoListaDoble(Object pElemento)
    //    {
    //        aElemento = pElemento;
    //        aSgte = null;
    //        aAnt = null;
    //    }
//
    //    public CNodoListaDoble(Object pElemento, CNodoListaDoble pSgte, CNodoListaDoble pAnt)
    //    {
    //        aElemento = pElemento;
    //        aSgte = pSgte;
    //        aAnt = pAnt;
    //    }
//
    //    public object Elemento
    //    {
    //        set { aElemento = value; }
    //        get { return aElemento; }
    //    }
//
    //    public CNodoListaDoble Sgte
    //    {
    //        set { aSgte = value; }
    //        get { return aSgte; }
    //    }
//
    //    public CNodoListaDoble Ant
    //    {
    //        set { aAnt = value; }
    //        get { return aAnt; }
    //    }
    //}
}
