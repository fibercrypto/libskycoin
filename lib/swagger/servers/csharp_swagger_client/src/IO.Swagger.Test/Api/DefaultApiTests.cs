/* 
 * Skycoin REST API.
 *
 * Skycoin is a next-generation cryptocurrency.
 *
 * OpenAPI spec version: 0.25.0
 * Contact: skycoin.doe@example.com
 * Generated by: https://github.com/swagger-api/swagger-codegen.git
 */

using System;
using System.IO;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.Reflection;
using RestSharp;
using NUnit.Framework;

using IO.Swagger.Client;
using IO.Swagger.Api;
using IO.Swagger.Model;

namespace IO.Swagger.Test
{
    /// <summary>
    ///  Class for testing DefaultApi
    /// </summary>
    /// <remarks>
    /// This file is automatically generated by Swagger Codegen.
    /// Please update the test case below to test the API endpoint.
    /// </remarks>
    [TestFixture]
    public class DefaultApiTests
    {
        private DefaultApi instance;

        /// <summary>
        /// Setup before each unit test
        /// </summary>
        [SetUp]
        public void Init()
        {
            instance = new DefaultApi();
        }

        /// <summary>
        /// Clean up after each unit test
        /// </summary>
        [TearDown]
        public void Cleanup()
        {

        }

        /// <summary>
        /// Test an instance of DefaultApi
        /// </summary>
        [Test]
        public void InstanceTest()
        {
            // TODO uncomment below to test 'IsInstanceOfType' DefaultApi
            //Assert.IsInstanceOfType(typeof(DefaultApi), instance, "instance is a DefaultApi");
        }

        
        /// <summary>
        /// Test AddressCount
        /// </summary>
        [Test]
        public void AddressCountTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //var response = instance.AddressCount();
            //Assert.IsInstanceOf<InlineResponse200> (response, "response is InlineResponse200");
        }
        
        /// <summary>
        /// Test CoinSupply
        /// </summary>
        [Test]
        public void CoinSupplyTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //instance.CoinSupply();
            
        }
        
        /// <summary>
        /// Test Csrf
        /// </summary>
        [Test]
        public void CsrfTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //var response = instance.Csrf();
            //Assert.IsInstanceOf<InlineResponse2001> (response, "response is InlineResponse2001");
        }
        
        /// <summary>
        /// Test DefaultConnections
        /// </summary>
        [Test]
        public void DefaultConnectionsTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //var response = instance.DefaultConnections();
            //Assert.IsInstanceOf<List<string>> (response, "response is List<string>");
        }
        
        /// <summary>
        /// Test Health
        /// </summary>
        [Test]
        public void HealthTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //var response = instance.Health();
            //Assert.IsInstanceOf<InlineResponse2002> (response, "response is InlineResponse2002");
        }
        
        /// <summary>
        /// Test NetworkConnection
        /// </summary>
        [Test]
        public void NetworkConnectionTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //string addr = null;
            //var response = instance.NetworkConnection(addr);
            //Assert.IsInstanceOf<InlineResponse2003> (response, "response is InlineResponse2003");
        }
        
        /// <summary>
        /// Test NetworkConnections
        /// </summary>
        [Test]
        public void NetworkConnectionsTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //string states = null;
            //string direction = null;
            //var response = instance.NetworkConnections(states, direction);
            //Assert.IsInstanceOf<List<InlineResponse2003>> (response, "response is List<InlineResponse2003>");
        }
        
        /// <summary>
        /// Test NetworkConnectionsDisconnect
        /// </summary>
        [Test]
        public void NetworkConnectionsDisconnectTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //string id = null;
            //instance.NetworkConnectionsDisconnect(id);
            
        }
        
        /// <summary>
        /// Test NetworkConnectionsExchange
        /// </summary>
        [Test]
        public void NetworkConnectionsExchangeTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //var response = instance.NetworkConnectionsExchange();
            //Assert.IsInstanceOf<List<string>> (response, "response is List<string>");
        }
        
        /// <summary>
        /// Test NetworkConnectionsTrust
        /// </summary>
        [Test]
        public void NetworkConnectionsTrustTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //var response = instance.NetworkConnectionsTrust();
            //Assert.IsInstanceOf<List<string>> (response, "response is List<string>");
        }
        
        /// <summary>
        /// Test ResendUnconfirmedTxns
        /// </summary>
        [Test]
        public void ResendUnconfirmedTxnsTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //instance.ResendUnconfirmedTxns();
            
        }
        
        /// <summary>
        /// Test VerifyAddress
        /// </summary>
        [Test]
        public void VerifyAddressTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //string address = null;
            //var response = instance.VerifyAddress(address);
            //Assert.IsInstanceOf<InlineResponse2009> (response, "response is InlineResponse2009");
        }
        
        /// <summary>
        /// Test Version
        /// </summary>
        [Test]
        public void VersionTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //instance.Version();
            
        }
        
        /// <summary>
        /// Test Wallet
        /// </summary>
        [Test]
        public void WalletTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //string id = null;
            //var response = instance.Wallet(id);
            //Assert.IsInstanceOf<WalletMeta> (response, "response is WalletMeta");
        }
        
        /// <summary>
        /// Test WalletBalance
        /// </summary>
        [Test]
        public void WalletBalanceTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //string id = null;
            //var response = instance.WalletBalance(id);
            //Assert.IsInstanceOf<InlineResponseDefault> (response, "response is InlineResponseDefault");
        }
        
        /// <summary>
        /// Test WalletFolder
        /// </summary>
        [Test]
        public void WalletFolderTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //string addr = null;
            //var response = instance.WalletFolder(addr);
            //Assert.IsInstanceOf<InlineResponse2008> (response, "response is InlineResponse2008");
        }
        
        /// <summary>
        /// Test WalletNewAddress
        /// </summary>
        [Test]
        public void WalletNewAddressTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //string id = null;
            //string num = null;
            //string password = null;
            //var response = instance.WalletNewAddress(id, num, password);
            //Assert.IsInstanceOf<InlineResponse2004> (response, "response is InlineResponse2004");
        }
        
        /// <summary>
        /// Test WalletNewSeed
        /// </summary>
        [Test]
        public void WalletNewSeedTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //string entropy = null;
            //var response = instance.WalletNewSeed(entropy);
            //Assert.IsInstanceOf<InlineResponse2005> (response, "response is InlineResponse2005");
        }
        
        /// <summary>
        /// Test WalletSeed
        /// </summary>
        [Test]
        public void WalletSeedTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //string id = null;
            //string password = null;
            //var response = instance.WalletSeed(id, password);
            //Assert.IsInstanceOf<InlineResponse2005> (response, "response is InlineResponse2005");
        }
        
        /// <summary>
        /// Test WalletUpdate
        /// </summary>
        [Test]
        public void WalletUpdateTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //string id = null;
            //string label = null;
            //var response = instance.WalletUpdate(id, label);
            //Assert.IsInstanceOf<InlineResponse2006> (response, "response is InlineResponse2006");
        }
        
        /// <summary>
        /// Test Wallets
        /// </summary>
        [Test]
        public void WalletsTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //var response = instance.Wallets();
            //Assert.IsInstanceOf<List<InlineResponse2007>> (response, "response is List<InlineResponse2007>");
        }
        
    }

}
