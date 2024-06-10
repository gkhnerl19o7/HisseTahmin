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
    //[DefaultClassOptions]
    
    public class Predictions : BaseObject
    {
        public virtual DateTime? Dates { get; set; }
        public virtual string PredictionPrices { get; set; }
        public virtual Stocks Stocks { get; set; }
        public Predictions()
        {
            // In the constructor, initialize collection properties, e.g.: 
            // this.AssociatedEntities = new ObservableCollection<AssociatedEntityObject>();
        }

       
    }
}