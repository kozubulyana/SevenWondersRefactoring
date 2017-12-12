using SevenWonders.DAL.Context;
using SevenWonders.WebAPI.DTO.Countries;
using SevenWonders.WebAPI.Models;
using System;
using System.Collections.Generic;
using System.Data.Entity;
using System.Linq;
using System.Web;

namespace SevenWonders.WebAPI.DAL.Countries
{
    public class CountriesRepository:ICountriesRepository, IDisposable
    {
        SevenWondersContext db;
        public CountriesRepository(SevenWondersContext context)
        {
            this.db = context;
        }
        public IEnumerable<Country> GetCountries()
        {
            var countries = db.Coutries.Where(x => !x.IsDeleted).OrderBy(x => x.Name).ToList();
            return countries;
        }
        public void AddCountry(CountryModel model)
        {
            if (model.Id == 0)
            {
                Country country = new Country()
                {
                    Id = model.Id,
                    Name = model.Name,
                    IsDeleted = false
                };
                db.Coutries.Add(country);
            }
            if (model.Id != 0)
            {
                Country country = db.Coutries.FirstOrDefault(x => x.Id == model.Id);
                country.Name = model.Name;
                db.Entry(country).State = EntityState.Modified;
            }
            db.SaveChanges();
        }
        public Country GetCountry(int id)
        {
            Country country = db.Coutries.FirstOrDefault(x => x.Id == id);
            return country;
        }
        public void DeleteCountry(int id)
        {
            Country country = db.Coutries.Find(id);
            country.IsDeleted = true;

            db.Entry(country).State = EntityState.Modified;
            db.SaveChanges();
        }
        public bool IsNameValid(int id, string name)
        {
            bool contain = db.Coutries
                .Where(x => !x.IsDeleted)
                .Any(x => x.Id != id && x.Name == name);

            return !contain;
        }

        private bool disposed = false;

        protected virtual void Dispose(bool disposing)
        {
            if (!this.disposed)
            {
                if (disposing)
                {
                    db.Dispose();
                }
            }
            this.disposed = true;
        }

        public void Dispose()
        {
            Dispose(true);
            GC.SuppressFinalize(this);
        }
    }
}