// <auto-generated>
/*
 * OpenAPI Petstore
 *
 * This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\
 *
 * The version of the OpenAPI document: 1.0.0
 * Generated by: https://github.com/openapitools/openapi-generator.git
 */

using System;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.IO;
using System.Text;
using System.Text.RegularExpressions;
using System.Text.Json;
using System.Text.Json.Serialization;
using System.ComponentModel.DataAnnotations;
using OpenAPIClientUtils = Org.OpenAPITools.Client.ClientUtils;

namespace Org.OpenAPITools.Model
{
    /// <summary>
    /// PolymorphicProperty
    /// </summary>
    public partial class PolymorphicProperty : IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="PolymorphicProperty" /> class.
        /// </summary>
        /// <param name="varBool"></param>
        [JsonConstructor]
        internal PolymorphicProperty(bool varBool)
        {
            VarBool = varBool;
            OnCreated();
        }

        /// <summary>
        /// Initializes a new instance of the <see cref="PolymorphicProperty" /> class.
        /// </summary>
        /// <param name="varString"></param>
        [JsonConstructor]
        internal PolymorphicProperty(string varString)
        {
            VarString = varString;
            OnCreated();
        }

        /// <summary>
        /// Initializes a new instance of the <see cref="PolymorphicProperty" /> class.
        /// </summary>
        /// <param name="varObject"></param>
        [JsonConstructor]
        internal PolymorphicProperty(Object varObject)
        {
            VarObject = varObject;
            OnCreated();
        }

        /// <summary>
        /// Initializes a new instance of the <see cref="PolymorphicProperty" /> class.
        /// </summary>
        /// <param name="list"></param>
        [JsonConstructor]
        internal PolymorphicProperty(List<string> list)
        {
            List = list;
            OnCreated();
        }

        partial void OnCreated();

        /// <summary>
        /// Gets or Sets VarBool
        /// </summary>
        public bool VarBool { get; set; }

        /// <summary>
        /// Gets or Sets VarString
        /// </summary>
        public string VarString { get; set; }

        /// <summary>
        /// Gets or Sets VarObject
        /// </summary>
        public Object VarObject { get; set; }

        /// <summary>
        /// Gets or Sets List
        /// </summary>
        public List<string> List { get; set; }

        /// <summary>
        /// Gets or Sets additional properties
        /// </summary>
        [JsonExtensionData]
        public Dictionary<string, JsonElement> AdditionalProperties { get; } = new Dictionary<string, JsonElement>();

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            StringBuilder sb = new StringBuilder();
            sb.Append("class PolymorphicProperty {\n");
            sb.Append("  AdditionalProperties: ").Append(AdditionalProperties).Append("\n");
            sb.Append("}\n");
            return sb.ToString();
        }

        /// <summary>
        /// To validate all properties of the instance
        /// </summary>
        /// <param name="validationContext">Validation context</param>
        /// <returns>Validation Result</returns>
        IEnumerable<System.ComponentModel.DataAnnotations.ValidationResult> IValidatableObject.Validate(ValidationContext validationContext)
        {
            yield break;
        }
    }

    /// <summary>
    /// A Json converter for type <see cref="PolymorphicProperty" />
    /// </summary>
    public class PolymorphicPropertyJsonConverter : JsonConverter<PolymorphicProperty>
    {
        /// <summary>
        /// Deserializes json to <see cref="PolymorphicProperty" />
        /// </summary>
        /// <param name="utf8JsonReader"></param>
        /// <param name="typeToConvert"></param>
        /// <param name="jsonSerializerOptions"></param>
        /// <returns></returns>
        /// <exception cref="JsonException"></exception>
        public override PolymorphicProperty Read(ref Utf8JsonReader utf8JsonReader, Type typeToConvert, JsonSerializerOptions jsonSerializerOptions)
        {
            int currentDepth = utf8JsonReader.CurrentDepth;

            if (utf8JsonReader.TokenType != JsonTokenType.StartObject && utf8JsonReader.TokenType != JsonTokenType.StartArray)
                throw new JsonException();

            JsonTokenType startingTokenType = utf8JsonReader.TokenType;

            while (utf8JsonReader.Read())
            {
                if (startingTokenType == JsonTokenType.StartObject && utf8JsonReader.TokenType == JsonTokenType.EndObject && currentDepth == utf8JsonReader.CurrentDepth)
                    break;

                if (startingTokenType == JsonTokenType.StartArray && utf8JsonReader.TokenType == JsonTokenType.EndArray && currentDepth == utf8JsonReader.CurrentDepth)
                    break;

                if (utf8JsonReader.TokenType == JsonTokenType.PropertyName && currentDepth == utf8JsonReader.CurrentDepth - 1)
                {
                    string propertyName = utf8JsonReader.GetString();
                    utf8JsonReader.Read();

                    switch (propertyName)
                    {
                        default:
                            break;
                    }
                }
            }

            Utf8JsonReader varBoolReader = utf8JsonReader;
            if (Client.ClientUtils.TryDeserialize<bool>(ref varBoolReader, jsonSerializerOptions, out bool varBool))
                return new PolymorphicProperty(varBool);

            Utf8JsonReader varStringReader = utf8JsonReader;
            if (Client.ClientUtils.TryDeserialize<string>(ref varStringReader, jsonSerializerOptions, out string varString))
                return new PolymorphicProperty(varString);

            Utf8JsonReader varObjectReader = utf8JsonReader;
            if (Client.ClientUtils.TryDeserialize<Object>(ref varObjectReader, jsonSerializerOptions, out Object varObject))
                return new PolymorphicProperty(varObject);

            Utf8JsonReader listReader = utf8JsonReader;
            if (Client.ClientUtils.TryDeserialize<List<string>>(ref listReader, jsonSerializerOptions, out List<string> list))
                return new PolymorphicProperty(list);

            throw new JsonException();
        }

        /// <summary>
        /// Serializes a <see cref="PolymorphicProperty" />
        /// </summary>
        /// <param name="writer"></param>
        /// <param name="polymorphicProperty"></param>
        /// <param name="jsonSerializerOptions"></param>
        /// <exception cref="NotImplementedException"></exception>
        public override void Write(Utf8JsonWriter writer, PolymorphicProperty polymorphicProperty, JsonSerializerOptions jsonSerializerOptions)
        {
            System.Text.Json.JsonSerializer.Serialize(writer, polymorphicProperty.VarBool, jsonSerializerOptions);

            System.Text.Json.JsonSerializer.Serialize(writer, polymorphicProperty.VarString, jsonSerializerOptions);

            System.Text.Json.JsonSerializer.Serialize(writer, polymorphicProperty.VarObject, jsonSerializerOptions);

            System.Text.Json.JsonSerializer.Serialize(writer, polymorphicProperty.List, jsonSerializerOptions);

            writer.WriteStartObject();

            writer.WriteEndObject();
        }
    }
}