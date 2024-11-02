import { Button } from "@/components/ui/button";
import React from "react";
import { LoadingButton } from "@/components/customShadcn/LoadingButton";

const Home = () => {
  return (
    <div className="flex flex-col min-h-screen justify-center items-center">
      <div className="container">
        <h1 className="text-3xl font-bold">Change Observer</h1>
        <div className="flex gap-2 items-center">
          <Button>Click me</Button>
          <LoadingButton>Loading</LoadingButton>
        </div>
      </div>
    </div>
  );
};

export default Home;
