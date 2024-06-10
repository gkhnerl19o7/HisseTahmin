using DevExpress.ExpressApp.EFCore.Updating;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Design;
using DevExpress.Persistent.BaseImpl.EF.PermissionPolicy;
using DevExpress.Persistent.BaseImpl.EF;
using DevExpress.ExpressApp.Design;
using DevExpress.ExpressApp.EFCore.DesignTime;

namespace Stock.Module.BusinessObjects;

// This code allows our Model Editor to get relevant EF Core metadata at design time.
// For details, please refer to https://supportcenter.devexpress.com/ticket/details/t933891.
public class StockContextInitializer : DbContextTypesInfoInitializerBase {
	protected override DbContext CreateDbContext() {
		var optionsBuilder = new DbContextOptionsBuilder<StockEFCoreDbContext>()
            .UseSqlServer(";")
            .UseChangeTrackingProxies()
            .UseObjectSpaceLinkProxies();
        return new StockEFCoreDbContext(optionsBuilder.Options);
	}
}
//This factory creates DbContext for design-time services. For example, it is required for database migration.
public class StockDesignTimeDbContextFactory : IDesignTimeDbContextFactory<StockEFCoreDbContext> {
	public StockEFCoreDbContext CreateDbContext(string[] args) {
		throw new InvalidOperationException("Make sure that the database connection string and connection provider are correct. After that, uncomment the code below and remove this exception.");
		//var optionsBuilder = new DbContextOptionsBuilder<StockEFCoreDbContext>();
		//optionsBuilder.UseSqlServer("Integrated Security=SSPI;Data Source=(localdb)\\mssqllocaldb;Initial Catalog=Stock");
        //optionsBuilder.UseChangeTrackingProxies();
        //optionsBuilder.UseObjectSpaceLinkProxies();
		//return new StockEFCoreDbContext(optionsBuilder.Options);
	}
}
[TypesInfoInitializer(typeof(StockContextInitializer))]
public class StockEFCoreDbContext : DbContext {
	public StockEFCoreDbContext(DbContextOptions<StockEFCoreDbContext> options) : base(options) {
	}
	public DbSet<Stocks> Stockss { get; set; }
    public DbSet<StocksPrices> StocksPricess { get; set; }
    public DbSet<Predictions> Predictionss { get; set; }

    protected override void OnModelCreating(ModelBuilder modelBuilder) {
        base.OnModelCreating(modelBuilder);
        modelBuilder.HasChangeTrackingStrategy(ChangeTrackingStrategy.ChangingAndChangedNotificationsWithOriginalValues);
        modelBuilder.UsePropertyAccessMode(PropertyAccessMode.PreferFieldDuringConstruction);
    }
}
