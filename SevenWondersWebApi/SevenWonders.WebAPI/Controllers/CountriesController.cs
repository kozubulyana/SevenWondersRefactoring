using SevenWonders.WebAPI.Models;
using System.Data.Entity;
using System.Linq;
using System.Web.Http;
using SevenWonders.DAL.Context;
using SevenWonders.WebAPI.DTO.Countries;
using SevenWonders.WebAPI.DAL;
using SevenWonders.WebAPI.DAL.Countries;

namespace SevenWonders.WebAPI.Controllers
{
    public class CountriesController : ApiController
    {
        private ICountriesRepository countriesRepository;

        public CountriesController()
        {
            this.countriesRepository = new CountriesRepository(new SevenWondersContext());
        }

        public CountriesController(ICountriesRepository countriesRepository)
        {
            this.countriesRepository = countriesRepository;
        }

        [HttpGet]
        public IHttpActionResult GetCountries()
        {
            var countries = countriesRepository.GetCountries();
            return Ok(countries);
        }

        [HttpPost]
        [Authorize(Roles = "manager, admin")]
        public void AddCountry([FromBody]CountryModel model)
        {
            if (ModelState.IsValid)
            {
                countriesRepository.AddCountry(model);
            }
        }

        [HttpGet]
        public IHttpActionResult GetCountry(int id)
        {
            Country country = countriesRepository.GetCountry(id);
            return Ok(country);
        }

        [HttpPost]
        [Authorize(Roles = "manager, admin")]
        public IHttpActionResult DeleteCountry([FromBody]int id)
        {
            countriesRepository.DeleteCountry(id);
            return Ok();
        }

        [HttpGet]
        public IHttpActionResult IsNameValid(int id, string name)
        {
            bool isValid = countriesRepository.IsNameValid(id, name);

            return Ok(isValid);
        }
    }
}