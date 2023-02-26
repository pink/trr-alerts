import requests
import json

def graphql_trr():
    accessToken = "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJ0aGVyZWFscmVhbC5jb20iLCJleHAiOjE2NTI5OTMwNTUsImlhdCI6MTY1Mjk5MTI1NSwiaXNzIjoidGhlcmVhbHJlYWwuY29tIiwianRpIjoiOTI3NjAzOWQtOWY5Ny00MjI0LTlmNTUtYjFkYWZiYTY1MGFkIiwibWVtIjoiIiwibmJmIjoxNjUyOTkxMjU0LCJzY3AiOltdLCJzbGciOiJkNWQxYzdiOS01ZTRmLTQ4YmItOTQyOS05ZWQxODE1MTE4NjYiLCJzdWIiOiIyNzY4NjI2NSIsInR5cCI6ImFjY2VzcyJ9.MK1-VPlHY0AC2maCRn4vS-XLoFFUOTYO8VT7NLZYVcjLITNw2FVDTKCK7LHEkLywlzlKAJTzn6QR2dWui_LnAw"

    cookies = {'_pxhd': 'blj1Fe2oPINs7gom5I5SYNEgtUrkIqQ3aYqTjSzzQcTOw-avR4J1RDqXHxMPTFK9s5xOrpBtZqODdQgnuBkb6w==:WroVa8dlRjREbSHmgUAU0/ToOyqew1jrayXonRXkT2PlG0bsY/YDrMTVFJBipjr0dQcI59p-6SEZTIH0I5iByr52F9dTh4cNsBXxFAqIQjA='}

    endpoint = f"https://api.therealreal.com/graphql"
    headers = {
        "Authorization": f"Bearer {accessToken}",
        "Api-Key": "49bd2b62cc5f48946f25d2eddb7177b8",
        "X-PX-AUTHORIZATION": "2:eyJ1IjoiYTcwZWYyOWEtZDdiMC0xMWVjLTljMDYtNDk1MTc0YWVjOWEzIiwidiI6IjFkNTQ2NWFmLWI4ZDYtMTFlYy04NzQzLTQ1NDM1MDRjNDQ1MSIsInQiOjE2NTI5OTE3MjYyNTUsImgiOiIwNjlkMGJkNGE1YzAwZDliNWRhZTc5OTZmZDVhZWY3OWI2MWM1YTE0OTdiYWY0NGViYTU2ZTIzNDJhN2VmNDkzIn0=",
        "User-Agent": "The RealReal/2.69.1 (com.realreal.shop; build:20220506.8388; iOS 15.4.1; Optional(\"iPhone12,3\")) Alamofire/2.69.1",
        "X-APOLLO-OPERATION-NAME": "fetchProductsWith",
        "Analytics-SessionId": "1652991255301",
        "Currency": "USD",
        "apollographql-client-name": "com.realreal.shop-apollo-ios",
        "apollographql-client-version": "2.69.1-20220506.8388",
        "Content-Length": "4425",
        "Connection": "keep-alive",
        "Membership": "general",
        "Accept-Language": "en-US;q=1.0",
        "anonymous-id": "6CDF4531-A134-449D-B101-D69A101AC14F",
        "Accept": "application/vnd.therealreal.v2+json",
        "X-APOLLO-OPERATION-TYPE": "query",
        "Content-Type": "application/json",
    }

    query = """query fetchProductsWith(
    $keyword: String
    $after: String = null
    $first: Int = 30
    $sortBy: SortBy = NEWEST
    $where: ProductFilters
    $currency: Currencies!
    $productIds: [String!]
    $saleId: String
    $saleSlug: String
    $savedSizes: Boolean = false
    $curbsideStoreIds: [Int]
  ) {
    products(
      after: $after
      first: $first
      query: $keyword
      sortBy: $sortBy
      where: $where
      currency: $currency
      productIds: $productIds
      saleId: $saleId
      saleSlug: $saleSlug
      savedSizes: $savedSizes
    ) {
      __typename
      ...productConnectionFragment
    }
  }
  fragment productConnectionFragment on ProductConnection {
    __typename
    abTest {
      __typename
      id
      name
      variant
    }
    aggregations {
      __typename
      facet_name: facetName
      name
      property
      ... on BucketAggregation {
        __typename
        ...leanBucketAggregationFragment
      }
      ... on BooleanAggregation {
        __typename
        selectedBoolean: selected
        value
      }
      ... on RangeAggregation {
        __typename
        ...aggregationRangeFragment
      }
    }
    edges {
      __typename
      cursor
      node {
        __typename
        ...leanProductFragment
      }
    }
    pageInfo {
      __typename
      ...pageInfoFragment
    }
    sortByOptions {
      __typename
      name
      options {
        __typename
        name
        value
      }
      property
      selected
    }
    taxons
    totalCount
    queryId
  }
  fragment leanBucketAggregationFragment on BucketAggregation {
    __typename
    buckets {
      __typename
      ...bucketFieldPropertiesFragment
    }
  }
  fragment bucketFieldPropertiesFragment on BucketField {
    __typename
    count
    images {
      __typename
      url
    }
    name
    selected
    value
  }
  fragment aggregationRangeFragment on RangeAggregation {
    __typename
    range {
      __typename
      maximum {
        __typename
        formatted
        raw
      }
      minimum {
        __typename
        formatted
        raw
      }
    }
    selectedRange: selected {
      __typename
      maximum {
        __typename
        formatted
        raw
      }
      minimum {
        __typename
        formatted
        raw
      }
    }
  }
  fragment leanProductFragment on Product {
    __typename
    variantId
    id
    url
    availability
    waitlisted
    obsessed
    images {
      __typename
      ...imageFragment
    }
    artist {
      __typename
      name
      description
      id
    }
    designer {
      __typename
      name
    }
    name
    attributes {
      __typename
      ...attributesFragment
    }
    price {
      __typename
      ...productPriceFragment
    }
    warehouseAvailability {
      __typename
      ...warehouseAvailabilityFragment
    }
    curbsidePickupStoreInfo(storeIds: $curbsideStoreIds) {
      __typename
      plpBadge
    }
    representative {
      __typename
      ...representativeProduct
    }
  }
  fragment imageFragment on Image {
    __typename
    height
    size
    url
    width
  }
  fragment attributesFragment on Attribute {
    __typename
    label
    type
    values
  }
  fragment productPriceFragment on Price {
    __typename
    discount
    final {
      __typename
      formatted
      usdCents
    }
    msrp {
      __typename
      formatted
      usdCents
    }
    original {
      __typename
      formatted
      usdCents
    }
  }
  fragment warehouseAvailabilityFragment on WarehouseAvailability {
    __typename
    checkoutShortText {
      __typename
      ...richText
    }
    checkoutText {
      __typename
      ...richText
    }
    globalShortText {
      __typename
      ...richText
    }
    globalText {
      __typename
      ...richText
    }
  }
  fragment richText on RichText {
    __typename
    enrichments {
      __typename
      attribute {
        __typename
        ... on Style {
          __typename
          value
        }
        ... on Link {
          __typename
          url
        }
      }
      end
      start
    }
    level
    text
    type
  }
  fragment representativeProduct on RepresentativeProduct {
    __typename
    id
    url
    variantId
  }
  fragment pageInfoFragment on PageInfo {
    __typename
    endCursor
    startCursor
    hasNextPage
    hasPreviousPage
  }"""
    # variables = {"after":'null',"curbsideStoreIds":[],"currency":"USD","first":30,"keyword":'null',"productIds":'null',"saleId":'null',"saleSlug":"mens-new-arrivals","sortBy":"NEWEST","where":{"booleans":[],"buckets":{"taxons":["1114"]},"ranges":{}}}

    r = requests.post(endpoint, json={"query": query, "variables": variables}, headers=headers, cookies=cookies)
    if r.status_code == 200:
        print(json.dumps(r.json(), indent=2))
    else:
        raise Exception(f"Query failed to run with a {r.status_code}.")

def main():
    spaceID = "mt0pmhki5db7"
    accessToken = "8c7dbd270cb98e83f9d8d57fb8a2ab7bac9d7501905fb013c69995ebf1b2a719"

    endpoint = f"https://graphql.contentful.com/content/v1/spaces/{spaceID}"
    headers = {"Authorization": f"Bearer {accessToken}"}

    query = """query {
        showCollection{
            items {
                title
                firstEpisodeDate
                lastEpisodeDate
                henshinMp4 {
                    url
                }
            }
        }
    }"""

    r = requests.post(endpoint, json={"query": query}, headers=headers)
    if r.status_code == 200:
        print(json.dumps(r.json(), indent=2))
    else:
        raise Exception(f"Query failed to run with a {r.status_code}.")

if __name__ == "__main__":
    graphql_trr()