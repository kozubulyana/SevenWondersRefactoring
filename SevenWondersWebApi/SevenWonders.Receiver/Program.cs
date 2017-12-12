using RabbitMQ.Client;
using RabbitMQ.Client.Events;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;
using SevenWonders.DAL.Context;
using SevenWonders.WebAPI.DTO.Account;
using SevenWonders.Receiver;

namespace _7Wonders.Receiver
{
    class Program
    {
        static void Main(string[] args)
        {
            RPCRequestReceiver.ReceiveRequest();
        }
    }
}
