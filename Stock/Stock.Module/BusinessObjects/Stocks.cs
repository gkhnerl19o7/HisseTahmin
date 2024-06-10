using DevExpress.Data.Filtering;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.DC;
using DevExpress.ExpressApp.Model;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl.EF;
using DevExpress.Persistent.Validation;
using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.ComponentModel;
using System.Linq;
using System.Runtime.CompilerServices;
using System.Text;

namespace Stock.Module.BusinessObjects
{
    [DefaultClassOptions]
    
    public class Stocks : BaseObject
    {
        public virtual string Name { get; set; }
        public virtual string Stockcode { get; set; } // Yaho finance daki hisse kodu 
        public virtual IList<StocksPrices> Stockprices { get; set; } = new ObservableCollection<StocksPrices>();
        public virtual IList<Predictions> Preds { get; set; } = new ObservableCollection<Predictions>();

        public Stocks()
        {
            // In the constructor, initialize collection properties, e.g.: 
            // this.AssociatedEntities = new ObservableCollection<AssociatedEntityObject>();
        }
    }
}