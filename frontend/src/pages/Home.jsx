import { Button } from "@/components/ui/button";
import React from "react";
import { useQuery } from "react-query";
import { useGetAllMarkers } from "@/apiQueries/queries";

const Home = () => {
  //custom hook to mutate marker query
  const { markers, isLoading, isError, isSuccess } = useGetAllMarkers();
  console.log(markers);

  return (
    <div className="flex flex-col min-h-screen justify-center items-center">
      <div className="container">
        <h1 className="text-3xl font-bold">Change Observer</h1>
        <div className="flex gap-2 items-center">
          <Button>Click me</Button>
        </div>
      </div>
    </div>
  );
};

export default Home;
