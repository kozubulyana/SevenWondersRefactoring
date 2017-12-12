using SevenWonders.WebAPI.DTO.Countries;
using SevenWonders.WebAPI.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace SevenWonders.WebAPI.DAL
{
    public interface ICountriesRepository : IDisposable
    {
        IEnumerable<Country> GetCountries();
        void AddCountry(CountryModel country);
        Country GetCountry(int id);
        void DeleteCountry(int id);
        bool IsNameValid(int id, string name);
    }
}